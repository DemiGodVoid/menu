#!/bin/bash

# Update package lists
echo "Updating package lists..."
apk update 

#install python 
echo "Installing python3..."
apk add python3 

# Install pip if not already installed
echo "Installing pip..."
apk add py3-pip

# Install the requests module using pip
echo "Installing requests module..."
pip3 install requests

echo "Installing selenium for website injections"
pip3 install selenium

# Install Node.js
echo "Installing node.js..."
apk add nodejs 
apk add npm 
npm install express multer

npm init -y
npm install express 
npm install multer

# Install Discord Bot library
echo "Installing discord.py..."
pip3 install discord.py

# Install other utilities
echo "Installing whois..."
sudo apt-get install -y whois
echo "Installing bs4"
pip3 install beautifulsoup4

# Install ngrok using snap
echo "Installing ngrok..."
curl -O https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
tar -xvzf ~/menu/ngrok-v3-stable-linux-arm64.tgz -C /usr/local/bin

echo "Installation complete."
