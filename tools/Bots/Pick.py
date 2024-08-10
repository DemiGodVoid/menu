import os

def main():
    print("Choose an option:")
    print("1. Discord Rekting bot")
    print("2. Normal Discord Bot")
    
    choice = input("Enter 1 or 2: ")
    
    if choice == '1':
        os.system("python3 DiscordRektBot.py")
    elif choice == '2':
        os.system("python3 NormalDiscordBot.py")
    else:
        print("Invalid choice. Please run the script again.")

if __name__ == "__main__":
    main()
