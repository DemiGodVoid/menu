import os
import signal
import psutil

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
                                                                                               (@_      (_     ^^     _)
                                                                                        _     ) \\_______\\__|IIIIII|__/__________________________
                                                                                       (_)@8@8{{}}<________|-\IIIIII/-|___________________________>
                                                                                              )_/        \\          /
                                                                                               (@          `--------`
                                                                                                         JOKAS NATION FOR LIFE
                                                                                                           Tool: HACKING MENU
                                                                                                       Version: 1.1.7-Alpha
                                                                                                      Made by:@B030BS on instagram
    """)
    print(f"{red}                                                                                        1: IP Tools.{reset}")
    print(f"{red}                                                                                        2: Phishers.{reset}")
    print(f"{red}                                                                                        3: Discord Bots.{reset}")
    print(f"{red}                                                                                        4: Pentesting Tools.{reset}")
    print(f"{red}                                                                                        5: Windows/Linux Backdoor.{reset}")
    print(f"{red}                                                                                             ---------------{reset}")
    print(f"{red}                                                                                        9: Install requirements{reset}")
    print(f"{red}                                                                                        10: Updates{reset}")
    print(f"{red}                                                                                        11: Update Tool{reset}")
    print(f"{red}                                                                                        12: Add ngrok auth token{reset}")
    print(f"{red}                                                                                        13: Kill processes on port 3000{reset}")
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
            # Start Pick.py in a new process and replace the current process
            os.execvp('python3', ['python3', 'tools/phishers/Pick.py'])

        elif choice == '3':
            # Start Pick.py in a new process and replace the current process
            os.execvp('python3', ['python3', 'tools/Bots/Pick.py'])
            
        elif choice == '4':
            # Start Pick.py in a new process and replace the current process
            os.execvp('python3', ['python3', 'tools/pentesting/Pick.py'])
            
        elif choice == '5':
            # Start Pick.py in a new process and replace the current process
            os.execvp('python3', ['python3', 'tools/backdoors/Pick.py'])
        elif choice == '9':
            os.system('bash install.sh')
            
        elif choice == '10':
            os.system('bash updates.sh')

        elif choice == '11':
            os.system('bash update.sh')
            
        elif choice == '12':
            os.system('python3 ngrok_auth.py')
            
        elif choice == '13':
            os.system('python3 open3000.py')
            
        elif choice == '0':
            print("\033[31mExiting...\033[0m")
            break
        else:
            print("\033[31mInvalid choice, please enter 1 or 0.\033[0m")

if __name__ == "__main__":
    main()
