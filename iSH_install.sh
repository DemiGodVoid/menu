#!/bin/bash

# Update package lists
echo "Updating package lists..."
apk update 

#install python 
echo "Installing python3..."
apk add python3 

#install bash 
echo "Installing bash..."
apk add bash 

#install psutil 
echo "Installing psutil..."
apk add py3-psutil 

# Install pip if not already installed
echo "Installing pip..."
apk add py3-pip

# Install the requests module using pip
echo "Installing requests module..."
pip3 install requests

echo "Installing selenium for website injections"
pip3 install selenium
pip3 install typing_extensions==4.7.1

# Install Node.js
echo "Installing node.js..."
apk add nodejs 
apk add npm 
npm install express multer

npm init -y
npm install express 
npm install multer

# Install other utilities
echo "Installing whois..."
apk add whois

echo "Installing bs4"
pip3 install beautifulsoup4

# Install Discord Bot library
echo "Installing discord.py..."
apk add py3-aiohttp
pip3 install discord.py

#!/bin/bash

# Install ngrok
echo "Installing ngrok..."

wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-arm64.tgz
tar -xvzf ~/ngrok-v3-stable-linux-arm64.tgz -C /usr/local/bin

echo "Installation complete."
