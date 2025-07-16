#!/usr/bin/env python3
"""
Quick setup script for Telegram Social Media Downloader Bot
"""

import os
import sys
import subprocess
import shutil

def run_command(command):
    """Run a shell command and return success status"""
    try:
        subprocess.run(command, shell=True, check=True)
        return True
    except subprocess.CalledProcessError:
        return False

def check_python_version():
    """Check if Python version is 3.8 or higher"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    print(f"✅ Python version: {sys.version.split()[0]}")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("📦 Installing dependencies...")
    if run_command("pip install -r requirements.txt"):
        print("✅ Dependencies installed successfully!")
        return True
    else:
        print("❌ Failed to install dependencies!")
        return False

def setup_environment():
    """Setup environment configuration"""
    if not os.path.exists('.env'):
        if os.path.exists('.env.example'):
            shutil.copy('.env.example', '.env')
            print("✅ Created .env file from template")
            print("⚠️  Please edit .env file with your bot token and channel information")
            return True
        else:
            print("❌ .env.example file not found!")
            return False
    else:
        print("✅ .env file already exists")
        return True

def create_downloads_dir():
    """Create downloads directory"""
    if not os.path.exists('downloads'):
        os.makedirs('downloads')
        print("✅ Created downloads directory")
    else:
        print("✅ Downloads directory already exists")

def main():
    """Main setup function"""
    print("🚀 Setting up Telegram Social Media Downloader Bot...")
    print("=" * 50)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        sys.exit(1)
    
    # Setup environment
    if not setup_environment():
        sys.exit(1)
    
    # Create downloads directory
    create_downloads_dir()
    
    print("=" * 50)
    print("🎉 Setup completed successfully!")
    print("\n📝 Next steps:")
    print("1. Edit .env file with your bot token")
    print("2. Add your channel ID to .env file")
    print("3. Run: python main.py")
    print("\n📚 For detailed instructions, see README.md")

if __name__ == "__main__":
    main()
