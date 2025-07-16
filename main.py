import os
import logging
import asyncio
import re
from typing import Optional
from urllib.parse import urlparse

import yt_dlp
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from telegram.error import TelegramError
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

class SocialMediaDownloaderBot:
    def __init__(self):
        self.bot_token = os.getenv('7989945714:AAHjm8FJv65KW4O6yCJC2Hadz-Ij2kopGsE')
        self.channel_id = os.getenv('CHANNEL_ID', '@mitakurd')
        self.channel_username = os.getenv('CHANNEL_USERNAME', 'mitakurd')
        self.channel_url = f"https://t.me/{self.channel_username}"
        
        if not self.bot_token:
            raise ValueError("7989945714:AAHjm8FJv65KW4O6yCJC2Hadz-Ij2kopGsE")
        
        # Supported social media patterns
        self.social_media_patterns = [
            r'(?:https?://)?(?:www\.)?(?:youtube\.com/watch\?v=|youtu\.be/)',
            r'(?:https?://)?(?:www\.)?instagram\.com/',
            r'(?:https?://)?(?:www\.)?tiktok\.com/',
            r'(?:https?://)?(?:www\.)?twitter\.com/',
            r'(?:https?://)?(?:www\.)?x\.com/',
            r'(?:https?://)?(?:www\.)?facebook\.com/',
            r'(?:https?://)?(?:www\.)?reddit\.com/',
            r'(?:https?://)?(?:www\.)?pinterest\.com/',
            r'(?:https?://)?(?:www\.)?snapchat\.com/',
            r'(?:https?://)?(?:www\.)?linkedin\.com/',
        ]
        
        # yt-dlp configuration
        self.ydl_opts = {
            'format': 'best[height<=720]/best',
            'outtmpl': 'downloads/%(title)s.%(ext)s',
            'noplaylist': True,
            'extractaudio': False,
            'audioformat': 'mp3',
            'embed_subs': True,
            'writesubtitles': False,
            'writeautomaticsub': False,
        }

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /start command"""
        user = update.effective_user
        welcome_message = f"""
🎬 **Welcome to Social Media Downloader Bot!** 🎬

Hi {user.first_name}! I can download content from:
• YouTube 📺
• Instagram 📸
• TikTok 🎵
• Twitter/X 🐦
• Facebook 📘
• And 1000+ other platforms!

**⚠️ IMPORTANT: You must join our channel first!**

👆 Click the button below to join, then send me any social media link!
        """
        
        keyboard = [[InlineKeyboardButton("🔔 Join Channel", url=self.channel_url)]]
        reply_markup = InlineKeyboardMarkup(keyboard)
        
        await update.message.reply_text(
            welcome_message,
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle /help command"""
        help_text = """
🔧 **How to use this bot:**

1️⃣ Join our channel: @mitakurd
2️⃣ Send me any social media link
3️⃣ Wait for download to complete
4️⃣ Enjoy your content!

**Supported platforms:**
• YouTube, Instagram, TikTok
• Twitter/X, Facebook, Reddit
• Pinterest, Snapchat, LinkedIn
• And many more!

**Commands:**
/start - Start the bot
/help - Show this help message
/status - Check your membership status
        """
        await update.message.reply_text(help_text, parse_mode='Markdown')

    async def check_membership(self, user_id: int, context: ContextTypes.DEFAULT_TYPE) -> bool:
        """Check if user is a member of the required channel"""
        try:
            member = await context.bot.get_chat_member(self.channel_id, user_id)
            return member.status in ['member', 'administrator', 'creator']
        except TelegramError as e:
            logger.error(f"Error checking membership: {e}")
            return False

    async def status_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Check user's membership status"""
        user_id = update.effective_user.id
        is_member = await self.check_membership(user_id, context)
        
        if is_member:
            await update.message.reply_text("✅ You are subscribed! Send me any social media link to download.")
        else:
            keyboard = [[InlineKeyboardButton("🔔 Join Channel", url=self.channel_url)]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(
                "❌ You need to join our channel first!",
                reply_markup=reply_markup
            )

    def is_social_media_link(self, text: str) -> bool:
        """Check if the text contains a social media link"""
        for pattern in self.social_media_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True
        return False

    async def download_content(self, url: str, update: Update) -> Optional[str]:
        """Download content from social media URL"""
        try:
            # Create downloads directory if it doesn't exist
            os.makedirs('downloads', exist_ok=True)
            
            with yt_dlp.YoutubeDL(self.ydl_opts) as ydl:
                # Extract info first
                info = ydl.extract_info(url, download=False)
                title = info.get('title', 'Unknown')
                duration = info.get('duration', 0)
                
                # Check file size (limit to 50MB for Telegram)
                filesize = info.get('filesize') or info.get('filesize_approx', 0)
                if filesize > 50 * 1024 * 1024:  # 50MB limit
                    await update.message.reply_text("❌ File too large (>50MB). Try a different quality or shorter video.")
                    return None
                
                # Download the content
                ydl.download([url])
                
                # Find the downloaded file
                for file in os.listdir('downloads'):
                    if title.replace('/', '_') in file or any(ext in file for ext in ['.mp4', '.mp3', '.jpg', '.png']):
                        return os.path.join('downloads', file)
                        
        except Exception as e:
            logger.error(f"Download error: {e}")
            await update.message.reply_text(f"❌ Download failed: {str(e)}")
            return None

    async def handle_message(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle incoming messages"""
        user_id = update.effective_user.id
        message_text = update.message.text
        
        # Check if user is subscribed to channel
        if not await self.check_membership(user_id, context):
            keyboard = [[InlineKeyboardButton("🔔 Join Channel", url=self.channel_url)]]
            reply_markup = InlineKeyboardMarkup(keyboard)
            await update.message.reply_text(
                "⚠️ **You must join our channel first!**\n\nClick the button below to join, then try again.",
                reply_markup=reply_markup,
                parse_mode='Markdown'
            )
            return
        
        # Check if message contains a social media link
        if not self.is_social_media_link(message_text):
            await update.message.reply_text(
                "❌ Please send a valid social media link!\n\n"
                "Supported: YouTube, Instagram, TikTok, Twitter, Facebook, and more!"
            )
            return
        
        # Send processing message
        processing_msg = await update.message.reply_text("🔄 Processing your link... Please wait!")
        
        try:
            # Download the content
            file_path = await self.download_content(message_text, update)
            
            if file_path and os.path.exists(file_path):
                # Send the file
                await processing_msg.edit_text("📤 Uploading your file...")
                
                with open(file_path, 'rb') as file:
                    if file_path.endswith(('.mp4', '.avi', '.mov', '.mkv')):
                        await update.message.reply_video(file)
                    elif file_path.endswith(('.mp3', '.wav', '.m4a')):
                        await update.message.reply_audio(file)
                    elif file_path.endswith(('.jpg', '.jpeg', '.png', '.gif')):
                        await update.message.reply_photo(file)
                    else:
                        await update.message.reply_document(file)
                
                # Clean up
                os.remove(file_path)
                await processing_msg.delete()
                
                # Success message
                await update.message.reply_text("✅ Download completed successfully!")
                
            else:
                await processing_msg.edit_text("❌ Failed to download content. Please try again or check the link.")
                
        except Exception as e:
            logger.error(f"Error handling message: {e}")
            await processing_msg.edit_text(f"❌ An error occurred: {str(e)}")

    async def error_handler(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """Handle errors"""
        logger.error(f"Update {update} caused error {context.error}")

    def run(self):
        """Start the bot"""
        application = Application.builder().token(self.bot_token).build()
        
        # Add handlers
        application.add_handler(CommandHandler("start", self.start))
        application.add_handler(CommandHandler("help", self.help_command))
        application.add_handler(CommandHandler("status", self.status_command))
        application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, self.handle_message))
        application.add_error_handler(self.error_handler)
        
        # Start the bot
        logger.info("Starting Social Media Downloader Bot...")
        application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    bot = SocialMediaDownloaderBot()
    bot.run()
