#!/bin/bash

# Navigate to the directory containing the server files
cd "$(dirname "$0")"

# Start the Node.js server
echo "Starting main server.js..."
node server3.js &

# Wait for the server to start
sleep 5

# Start ngrok
echo "Starting ngrok..."
ngrok http 3000 

# Wait for user input to stop the script
echo "Press [Enter] to stop..."
read
