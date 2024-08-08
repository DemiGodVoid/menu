import os

def display_menu():
    print("1: IP Tools")
    print("0: Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            os.system('python tools/ip_tools/ipinfo.py')
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter 1 or 0.")

if __name__ == "__main__":
    main()
