#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt-get update

# Install pip if not already installed
echo "Installing pip..."
sudo apt-get install -y python3-pip

# Install the requests module using pip
echo "Installing requests module..."
pip3 install requests

echo "Installing selenium for website injections"
pip install selenium


# Install ngrok using snap
echo "Installing ngrok..."
sudo snap install ngrok

# Install Node.js
echo "Installing node.js..."
sudo apt install -y nodejs npm
npm install
npm install express multer

npm init -y
npm install express multer

# Install Discord Bot library
echo "Installing discord.py..."
pip3 install discord.py

# Install other utilities
echo "Installing whois..."
sudo apt-get install -y whois
echo "Installing bs4"
pip3 install beautifulsoup4

echo "Installation complete."
