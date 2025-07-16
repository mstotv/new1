# 🎬 Telegram Social Media Downloader Bot

A powerful Telegram bot that downloads content from 1000+ social media platforms with mandatory channel subscription verification.

## ✨ Features

- **Universal Downloader**: Supports YouTube, Instagram, TikTok, Twitter/X, Facebook, Reddit, Pinterest, and 1000+ other platforms
- **Channel Subscription**: Mandatory subscription to @mitakurd before using the bot
- **Smart Detection**: Automatically detects and processes social media links
- **File Management**: Handles videos, images, and audio files up to 50MB
- **User-Friendly**: Interactive buttons and clear status messages
- **Error Handling**: Comprehensive error handling and user feedback
- **Security**: Secure token management and environment configuration

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Telegram Bot Token (from @BotFather)
- Your channel ID for membership verification

### Local Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd telegram_downloader_bot
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` file with your credentials:
   ```env
   BOT_TOKEN=7989945714:AAHjm8FJv65KW4O6yCJC2Hadz-Ij2kopGsE
   CHANNEL_ID=@mitakurd
   CHANNEL_USERNAME=mitakurd
   ```

4. **Run the bot**
   ```bash
   python main.py
   ```

## 🔧 Getting Your Bot Token

1. Open Telegram and search for @BotFather
2. Send `/newbot` command
3. Choose a name and username for your bot
4. Copy the token provided by BotFather
5. Paste it in your `.env` file

## 🔍 Getting Your Channel ID

### Method 1: Using @userinfobot
1. Add @userinfobot to your channel
2. Send any message in the channel
3. The bot will reply with channel information including ID

### Method 2: Using Telegram Web
1. Open your channel in Telegram Web
2. Look at the URL: `https://web.telegram.org/k/#-1001500958084`
3. The number after `-100` is your channel ID

## 🌐 Deployment Options

### Option 1: Railway (Recommended)

1. **Create Railway Account**: Go to [railway.app](https://railway.app)
2. **Connect GitHub**: Link your GitHub account
3. **Deploy Project**:
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your bot repository
4. **Set Environment Variables**:
   - Go to Variables tab
   - Add `BOT_TOKEN` 7989945714:AAHjm8FJv65KW4O6yCJC2Hadz-Ij2kopGsE
   - Add `CHANNEL_ID` 1001500958084
   - Add `CHANNEL_USERNAME` mitakurd
5. **Deploy**: Railway will automatically build and deploy your bot

**Cost**: Free tier available, then ~$5/month

### Option 2: Heroku

1. **Install Heroku CLI**: Download from [heroku.com](https://heroku.com)
2. **Login to Heroku**:
   ```bash
   heroku login
   ```
3. **Create Heroku App**:
   ```bash
   heroku create MitaKurdBot
   ```
4. **Set Environment Variables**:
   ```bash
   heroku config:set BOT_TOKEN=7989945714:AAHjm8FJv65KW4O6yCJC2Hadz-Ij2kopGsE
   heroku config:set CHANNEL_ID=@mitakurd
   heroku config:set CHANNEL_USERNAME=mitakurd
   ```
5. **Deploy**:
   ```bash
   git add .
   git commit -m "Deploy bot"
   git push heroku main
   ```

**Cost**: ~$7/month (no free tier)

### Option 3: DigitalOcean App Platform

1. **Create DigitalOcean Account**: Go to [digitalocean.com](https://digitalocean.com)
2. **Create New App**: 
   - Go to Apps → Create App
   - Connect your GitHub repository
3. **Configure Build Settings**:
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `python main.py`
4. **Set Environment Variables**:
   - Add `BOT_TOKEN`, `CHANNEL_ID`, `CHANNEL_USERNAME`
5. **Deploy**: Click "Create Resources"

**Cost**: ~$5/month

### Option 4: VPS (Ubuntu/Debian)

1. **Connect to your VPS**:
   ```bash
   ssh root@your-server-ip
   ```

2. **Update system**:
   ```bash
   apt update && apt upgrade -y
   ```

3. **Install Python and Git**:
   ```bash
   apt install python3 python3-pip git -y
   ```

4. **Clone repository**:
   ```bash
   git clone <your-repo-url>
   cd telegram_downloader_bot
   ```

5. **Install dependencies**:
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Configure environment**:
   ```bash
   cp .env.example .env
   nano .env  # Edit with your tokens
   ```

7. **Install process manager**:
   ```bash
   pip3 install supervisor
   ```

8. **Create supervisor config** (`/etc/supervisor/conf.d/telegram_bot.conf`):
   ```ini
   [program:telegram_bot]
   command=python3 /path/to/telegram_downloader_bot/main.py
   directory=/path/to/telegram_downloader_bot
   user=root
   autostart=true
   autorestart=true
   stderr_logfile=/var/log/telegram_bot.err.log
   stdout_logfile=/var/log/telegram_bot.out.log
   ```

9. **Start the bot**:
   ```bash
   supervisorctl reread
   supervisorctl update
   supervisorctl start telegram_bot
   ```

**Cost**: $5-20/month depending on VPS provider

## 📱 Bot Commands

- `/start` - Welcome message and channel join prompt
- `/help` - Show help and supported platforms
- `/status` - Check your membership status

## 🔒 Security Features

- **Environment Variables**: Secure token storage
- **Input Validation**: Validates social media URLs
- **Error Handling**: Comprehensive error management
- **File Size Limits**: Prevents large file downloads
- **Membership Verification**: Ensures channel subscription

## 🛠️ Supported Platforms

- YouTube (videos, playlists, shorts)
- Instagram (posts, stories, reels, IGTV)
- TikTok (videos, sounds)
- Twitter/X (videos, images, GIFs)
- Facebook (videos, images)
- Reddit (videos, images, GIFs)
- Pinterest (images, videos)
- Snapchat (public content)
- LinkedIn (videos, images)
- And 1000+ more platforms via yt-dlp

## 📊 File Format Support

- **Videos**: MP4, AVI, MOV, MKV, WebM
- **Audio**: MP3, WAV, M4A, OGG
- **Images**: JPG, PNG, GIF, WebP

## ⚙️ Configuration Options

Edit your `.env` file to customize:

```env
# Required
BOT_TOKEN=your_bot_token_here
CHANNEL_ID=@mitakurd
CHANNEL_USERNAME=mitakurd

# Optional
LOG_LEVEL=INFO          # Logging level (DEBUG, INFO, WARNING, ERROR)
MAX_FILE_SIZE=50        # Maximum file size in MB
DOWNLOAD_TIMEOUT=300    # Download timeout in seconds
```

## 🐛 Troubleshooting

### Common Issues

1. **Bot not responding**:
   - Check if bot token is correct
   - Verify bot is running without errors
   - Check internet connection

2. **Channel verification failing**:
   - Ensure channel ID is correct (include @ symbol)
   - Make sure bot is added to the channel as admin
   - Check if channel is public

3. **Download failures**:
   - Some platforms may block automated downloads
   - File might be too large (>50MB limit)
   - URL might be invalid or expired

4. **Deployment issues**:
   - Check all environment variables are set
   - Verify Python version compatibility
   - Check hosting provider logs

### Getting Help

If you encounter issues:
1. Check the logs for error messages
2. Verify all configuration settings
3. Test with different social media links
4. Check hosting provider status

## 📝 License

This project is for educational purposes. Please respect the terms of service of social media platforms and copyright laws.

## 🔄 Updates

To update your bot:
1. Pull latest changes from repository
2. Update dependencies: `pip install -r requirements.txt`
3. Restart your bot service

## 💡 Tips

- Test your bot with various social media links
- Monitor your hosting provider's resource usage
- Keep your bot token secure and never share it
- Regularly update dependencies for security
- Consider implementing rate limiting for heavy usage

---

**Made with ❤️ for @mitakurd community**
