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

echo "Installation complete."
