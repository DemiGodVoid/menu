#!/bin/bash

# ANSI escape codes for red text
RED='\033[0;31m'
NC='\033[0m'  # No color

# Change to the home directory
cd ~

# Remove the existing t.g.s directory if it exists
if [ -d "t.g.s" ]; then
    echo -e "${RED}Removing existing t.g.s directory...${NC}"
    rm -rf t.g.s
else
    echo -e "${RED}t.g.s directory does not exist. Proceeding with cloning...${NC}"
fi

# Clone the repository from GitHub
echo -e "${RED}Cloning the repository...${NC}"
git clone https://github.com/DemiGodVoid/t.g.s

echo -e "${RED}Update complete.${NC}"
