import os

def display_menu():
    print("""
                                                                     ______
                                                                  .-"      "-.
                                                                /            \\
                                                               |              |
                                                               |,  .-.   .-.  ,|
                                                               | )(_o/  \\o_)( |
                                                               |/     /\\     \\|
                                                      (@_       (_     ^^     _)
                                               _     ) \\_______\\__|IIIIII|__/__________________________
                                               (_)@8@8{}<________|-\IIIIII/-|___________________________>
                                                     )_/        \\          /
                                                     (@           `--------`
                                                                 THE GHOST SQUAD
                                                                  Tool: T.G.S
                                                               Version: 1.0.0-Alpha
                                                  Made by: VOID(@ruggedbert on kik/@kiksucks on discord)
    """)
    print("                                                1: IP Tools")
    print("                                                2: Phishers(Gps pin pointer/Camera Phisher)")
    print("                                                         ---------------")
    print("                                                9: Install requirements")
    print("                                                10: Updates")
    print("                                                11: Update Tool")
    print("                                                0: Exit")

def clear_screen():
    os.system('clear')  # Clear the screen

def main():
    while True:
        clear_screen()  # Clear the screen at the start of each loop
        display_menu()
        choice = input("                                                Enter your choice: ").strip()
        
        if choice == '1':
            os.system('python3 tools/ip_tools/ipinfo.py')

        elif choice == '2':
            os.system('bash tools/phishers/pick.sh')

        elif choice == '9':
            os.system('bash install.sh')
            
        elif choice == '10':
            os.system('bash updates.sh')

        elif choice == '11':
            os.system('bash update.sh')
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice, please enter 1 or 0.")

if __name__ == "__main__":
    main()
