import requests
import subprocess

# Define ANSI escape codes for red text
RED_TEXT = '\033[91m'
RESET_TEXT = '\033[0m'

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"{RED_TEXT}Error: Unable to fetch data (status code: {response.status_code}){RESET_TEXT}")
        return {}

def whois_lookup(ip):
    try:
        result = subprocess.run(['whois', ip], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"{RED_TEXT}Error during WHOIS lookup: {str(e)}{RESET_TEXT}"

def dns_lookup(ip):
    try:
        result = subprocess.run(['nslookup', ip], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"{RED_TEXT}Error during DNS lookup: {str(e)}{RESET_TEXT}"

def main():
    ip = input(f"{RED_TEXT}Enter the IP address you want to get information about: {RESET_TEXT}")
    info = get_ip_info(ip)
    
    print(f"\n{RED_TEXT}Detailed IP Information:{RESET_TEXT}")
    print(f"  {RED_TEXT}ip:{RESET_TEXT} {info.get('ip', 'N/A')}")
    print(f"  {RED_TEXT}hostname:{RESET_TEXT} {info.get('hostname', 'N/A')}")
    print(f"  {RED_TEXT}city:{RESET_TEXT} {info.get('city', 'N/A')}")
    print(f"  {RED_TEXT}region:{RESET_TEXT} {info.get('region', 'N/A')}")
    print(f"  {RED_TEXT}country:{RESET_TEXT} {info.get('country', 'N/A')}")
    print(f"  {RED_TEXT}loc:{RESET_TEXT} {info.get('loc', 'N/A')}")
    print(f"  {RED_TEXT}org:{RESET_TEXT} {info.get('org', 'N/A')}")
    print(f"  {RED_TEXT}postal:{RESET_TEXT} {info.get('postal', 'N/A')}")
    print(f"  {RED_TEXT}timezone:{RESET_TEXT} {info.get('timezone', 'N/A')}")
    print(f"  {RED_TEXT}readme:{RESET_TEXT} {info.get('readme', 'N/A')}")
    
    print(f"\n{RED_TEXT}IP Information:{RESET_TEXT}")
    print(f"{RED_TEXT}IP:{RESET_TEXT} {info.get('ip', 'N/A')}")
    print(f"{RED_TEXT}City:{RESET_TEXT} {info.get('city', 'N/A')}")
    print(f"{RED_TEXT}Region:{RESET_TEXT} {info.get('region', 'N/A')}")
    print(f"{RED_TEXT}Country:{RESET_TEXT} {info.get('country', 'N/A')}")
    print(f"{RED_TEXT}Location:{RESET_TEXT} {info.get('loc', 'N/A')}")
    print(f"{RED_TEXT}ISP:{RESET_TEXT} {info.get('org', 'N/A')}")
    
    print(f"\n{RED_TEXT}Performing WHOIS lookup...{RESET_TEXT}")
    whois_info = whois_lookup(ip)
    print(whois_info)
    
    print(f"\n{RED_TEXT}Performing DNS lookup...{RESET_TEXT}")
    dns_info = dns_lookup(ip)
    print(dns_info)
    
    # Pause until a key is pressed
    input(f"\n{RED_TEXT}Press Enter to continue...{RESET_TEXT}")

if __name__ == "__main__":
    main()
