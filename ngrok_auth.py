import subprocess 
import time 

def add_token():
    print("\033[31mAcquire ngrok token at\033[0m ")
    token = input("\033[31mPlease enter your ngrok token:\033[0m ")
    command = f"ngrok config add-authtoken {token}"
    try:
        subprocess.run(command, shell=True, check=True)
        print("\033[31mNgrok authtoken added successfully.\033[0m")
        time.sleep(3)
        os.system('python3 start.py')
    except subprocess.CalledProcessError as e:
        print(f"\033[31mAn error occurred while adding the authtoken:\033[0m {e}")
        time.sleep(3)
        os.system('python3 ngrok_auth.py')
add_token()
