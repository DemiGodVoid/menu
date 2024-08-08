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

# Install ngrok using snap
echo "Installing ngrok..."
sudo snap install ngrok

# Install Node.js
echo "Installing node.js..."
sudo apt install nodejs npm
npm install
npm install express multer
npm install express

npm init -y
npm install express multer

#Install others
sudo apt-get install whois

echo "Installation complete."
