# 🚀 Deployment Guide

This guide provides step-by-step instructions for deploying your Telegram Social Media Downloader Bot to various hosting platforms.

## 📋 Prerequisites

Before deploying, ensure you have:
- ✅ Telegram Bot Token (from @BotFather)
- ✅ Channel ID for @mitakurd
- ✅ GitHub account (for most hosting options)
- ✅ All bot files ready

## 🔧 Getting Your Bot Token

1. Open Telegram and search for **@BotFather**
2. Send `/newbot` command
3. Choose a name: `Social Media Downloader`
4. Choose a username: `your_bot_username_bot`
5. Copy the token provided (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

## 🆔 Getting Your Channel ID

### Method 1: Using @userinfobot
1. Add @userinfobot to your @mitakurd channel
2. Send any message in the channel
3. Bot will reply with channel info including ID (format: `-1001234567890`)

### Method 2: Using Telegram Web
1. Open https://web.telegram.org/k/
2. Navigate to your @mitakurd channel
3. Check URL: `https://web.telegram.org/k/#-1001234567890`
4. Copy the number after `-100`

---

## 🌐 Hosting Options

### Option 1: Railway (Recommended - Easiest)

**Cost**: Free tier → $5/month  
**Difficulty**: ⭐⭐☆☆☆

#### Steps:

1. **Create Railway Account**
   - Go to [railway.app](https://railway.app)
   - Sign up with GitHub

2. **Upload Code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git remote add origin https://github.com/yourusername/telegram-bot.git
   git push -u origin main
   ```

3. **Deploy on Railway**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your bot repository
   - Railway will auto-detect Python and deploy

4. **Set Environment Variables**
   - Go to your project → Variables tab
   - Add these variables:
     ```
     BOT_TOKEN=your_bot_token_here
     CHANNEL_ID=@mitakurd
     CHANNEL_USERNAME=mitakurd
     ```

5. **Deploy**
   - Railway automatically deploys
   - Check logs to ensure bot is running
   - Bot should be live within 2-3 minutes

---

### Option 2: Heroku

**Cost**: $7/month (no free tier)  
**Difficulty**: ⭐⭐⭐☆☆

#### Steps:

1. **Install Heroku CLI**
   - Download from [heroku.com](https://heroku.com)
   - Install and restart terminal

2. **Login to Heroku**
   ```bash
   heroku login
   ```

3. **Create Heroku App**
   ```bash
   heroku create your-bot-name
   ```

4. **Set Environment Variables**
   ```bash
   heroku config:set BOT_TOKEN=your_bot_token_here
   heroku config:set CHANNEL_ID=@mitakurd
   heroku config:set CHANNEL_USERNAME=mitakurd
   ```

5. **Deploy**
   ```bash
   git add .
   git commit -m "Deploy to Heroku"
   git push heroku main
   ```

6. **Scale Worker**
   ```bash
   heroku ps:scale worker=1
   ```

---

### Option 3: DigitalOcean App Platform

**Cost**: $5/month  
**Difficulty**: ⭐⭐⭐☆☆

#### Steps:

1. **Create DigitalOcean Account**
   - Go to [digitalocean.com](https://digitalocean.com)
   - Sign up and verify account

2. **Create App**
   - Go to Apps → Create App
   - Connect GitHub repository
   - Select your bot repository

3. **Configure Build Settings**
   - Build Command: `pip install -r requirements.txt`
   - Run Command: `python main.py`

4. **Set Environment Variables**
   - Go to Settings → Environment Variables
   - Add:
     ```
     BOT_TOKEN=your_bot_token_here
     CHANNEL_ID=@mitakurd
     CHANNEL_USERNAME=mitakurd
     ```

5. **Deploy**
   - Click "Create Resources"
   - Wait for deployment (5-10 minutes)

---

### Option 4: VPS (Ubuntu/Debian)

**Cost**: $5-20/month  
**Difficulty**: ⭐⭐⭐⭐⭐

#### Steps:

1. **Connect to VPS**
   ```bash
   ssh root@your-server-ip
   ```

2. **Update System**
   ```bash
   apt update && apt upgrade -y
   ```

3. **Install Dependencies**
   ```bash
   apt install python3 python3-pip git supervisor -y
   ```

4. **Clone Repository**
   ```bash
   cd /opt
   git clone https://github.com/yourusername/telegram-bot.git
   cd telegram-bot
   ```

5. **Install Python Packages**
   ```bash
   pip3 install -r requirements.txt
   ```

6. **Configure Environment**
   ```bash
   cp .env.example .env
   nano .env
   ```
   
   Add your credentials:
   ```env
   BOT_TOKEN=your_bot_token_here
   CHANNEL_ID=@mitakurd
   CHANNEL_USERNAME=mitakurd
   ```

7. **Create Supervisor Config**
   ```bash
   nano /etc/supervisor/conf.d/telegram_bot.conf
   ```
   
   Add:
   ```ini
   [program:telegram_bot]
   command=python3 /opt/telegram-bot/main.py
   directory=/opt/telegram-bot
   user=root
   autostart=true
   autorestart=true
   stderr_logfile=/var/log/telegram_bot.err.log
   stdout_logfile=/var/log/telegram_bot.out.log
   ```

8. **Start Bot Service**
   ```bash
   supervisorctl reread
   supervisorctl update
   supervisorctl start telegram_bot
   ```

9. **Check Status**
   ```bash
   supervisorctl status telegram_bot
   ```

---

## ✅ Verification Steps

After deployment, verify your bot works:

1. **Find Your Bot**
   - Search for your bot username in Telegram
   - Start a conversation

2. **Test Commands**
   - Send `/start` - Should show welcome message
   - Send `/help` - Should show help text
   - Send `/status` - Should check membership

3. **Test Download**
   - Join @mitakurd channel first
   - Send a YouTube link
   - Bot should download and send the video

## 🐛 Troubleshooting

### Common Issues:

**Bot not responding:**
- ✅ Check bot token is correct
- ✅ Verify environment variables are set
- ✅ Check hosting platform logs

**Channel verification failing:**
- ✅ Ensure channel ID includes @ symbol
- ✅ Make sure channel is public
- ✅ Verify bot has access to channel info

**Download failures:**
- ✅ Check internet connection on server
- ✅ Verify yt-dlp is installed correctly
- ✅ Test with different social media links

**Deployment errors:**
- ✅ Check Python version (3.8+ required)
- ✅ Verify all dependencies in requirements.txt
- ✅ Check hosting platform documentation

### Getting Logs:

**Railway:** Project → Deployments → View Logs  
**Heroku:** `heroku logs --tail`  
**DigitalOcean:** App → Runtime Logs  
**VPS:** `tail -f /var/log/telegram_bot.out.log`

## 🔄 Updates

To update your bot:

1. **Update code locally**
2. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Update bot"
   git push
   ```
3. **Redeploy** (automatic for most platforms)

## 💡 Pro Tips

- **Monitor Usage**: Keep an eye on bandwidth and storage
- **Backup Config**: Save your environment variables securely
- **Update Dependencies**: Regularly update yt-dlp and other packages
- **Rate Limiting**: Consider adding rate limits for heavy usage
- **Logging**: Monitor logs for errors and usage patterns

## 🆘 Support

If you encounter issues:
1. Check the troubleshooting section above
2. Review hosting platform documentation
3. Test locally first to isolate issues
4. Check bot permissions and channel settings

---

**🎉 Congratulations! Your bot should now be live and ready to download social media content for @mitakurd subscribers!**
