#!/bin/bash

# Clear the terminal
clear

# Display menu options
echo "1. Cam Phish"
echo "0. Exit"

# Read user input
read -p "Choose an option: " choice

# Handle user input
case $choice in
    1)
        # Run camphish.sh
        bash /root/t.g.s/tools/phishers/camphish.sh
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
