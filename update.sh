#!/bin/bash

# Change to the home directory
cd ~

# Remove the existing t.g.s directory if it exists
if [ -d "t.g.s" ]; then
    echo "Removing existing t.g.s directory..."
    rm -rf t.g.s
else
    echo "t.g.s directory does not exist. Proceeding with cloning..."
fi

# Clone the repository from GitHub
echo "Cloning the repository..."
git clone https://github.com/DemiGodVoid/t.g.s

echo "Update complete."
