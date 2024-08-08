#!/bin/bash

# Echo commands to the terminal
echo "Starting main server.js..."

# Run server.js with Node.js
node server2.js &

# Start ngrok (adjust the command if needed for your setup)
echo "Starting ngrok..."
ngrok http 3000 &

# Wait for user input to keep the script running
read -p "Press [Enter] to stop..."
