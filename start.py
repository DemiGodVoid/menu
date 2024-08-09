import os

def display_menu():
    red = "\033[31m"  # ANSI escape code for red text
    reset = "\033[0m"  # ANSI escape code to reset the color
    print(f"""{red}
                                                                                                             ______
                                                                                                          .-"      "-.
                                                                                                         /            \\
                                                                                                        |              |
                                                                                                        |,  .-.   .-.  ,|
                                                                                                        | )(_o/  \\o_)( |
                                                                                                        |/     /\\     \\|
                                                                                               (@_       (_     ^^     _)
                                                                                        _     ) \\_______\\__|IIIIII|__/__________________________
                                                                                      (_)@8@8{{}}<________|-\IIIIII/-|___________________________>
                                                                                              )_/        \\          /
                                                                                               (@          `--------`
                                                                                                         THE GHOST SQUAD
                                                                                                           Tool: T.G.S
                                                                                                       Version: 1.0.1-Alpha
                                                                                         Made by: VOID(@ruggedbert on kik/@kiksucks on discord)
    """)
    print(f"{red}                                                                                        1: IP Tools{reset}")
    print(f"{red}                                                                                        2: Phishers(Gps pin pointer/Camera Phisher){reset}")
    print(f"{red}                                                                                             ---------------{reset}")
    print(f"{red}                                                                                        9: Install requirements{reset}")
    print(f"{red}                                                                                        10: Updates{reset}")
    print(f"{red}                                                                                        11: Update Tool{reset}")
    print(f"{red}                                                                                        0: Exit{reset}")

def clear_screen():
    os.system('clear')  # Clear the screen

def main():
    while True:
        clear_screen()  # Clear the screen at the start of each loop
        display_menu()
        choice = input("\033[31m                                                                                     Enter your choice: \033[0m").strip()
        
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
            print("\033[31mExiting...\033[0m")
            break
        else:
            print("\033[31mInvalid choice, please enter 1 or 0.\033[0m")

if __name__ == "__main__":
    main()
