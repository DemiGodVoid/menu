#!/bin/bash

# Update package lists
echo "Updating package lists..."
pkg update -y

# Install pip if not already installed
echo "Installing pip..."
pkg install -y python-pip

# Install the requests module using pip
echo "Installing requests module..."
pip install requests

# Install Node.js
echo "Installing Node.js..."
pkg install -y nodejs
npm install
npm install express multer

npm init -y
npm install express multer

# Install ngrok manually
echo "Installing ngrok..."
pkg install -y wget
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-stable-linux-arm.zip
unzip ngrok-stable-linux-arm.zip
chmod +x ngrok
mv ngrok $PREFIX/bin/

# Install Discord Bot library
echo "Installing discord.py..."
pip install discord.py

# Install other utilities
echo "Installing whois..."
pkg install -y whois

echo "Installation complete."
