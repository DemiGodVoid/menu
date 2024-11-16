#!/bin/bash

# Update package lists
echo "Updating package lists..."
sudo apt-get update

# Install pip if not already installed
echo "Installing pip..."
sudo apt-get install -y python3-pip

# Install the requests module using pip
echo "Installing requests module..."
sudo apt install python3-requests
echo "Installing selenium for website injections"
sudo apt install python3-selenium

echo "Updating package list..."
sudo apt-get update

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
sudo apt install python3-discord

# Install other utilities
echo "Installing whois..."
sudo apt-get install -y whois
echo "Installing bs4"
sudo apt install python3-bs4

echo "Verifying installation..."
sudo python3 -c "import requests; import selenium; import discord; import bs4"

echo "Installation complete."
if [ $? -eq 0 ]; then
    echo "All dependencies installed successfully."
else
    echo "There was an error in installation."
fi
