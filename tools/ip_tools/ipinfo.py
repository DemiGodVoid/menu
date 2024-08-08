import requests
import subprocess

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data (status code: {response.status_code})")
        return {}

def whois_lookup(ip):
    try:
        result = subprocess.run(['whois', ip], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error during WHOIS lookup: {str(e)}"

def dns_lookup(ip):
    try:
        result = subprocess.run(['nslookup', ip], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error during DNS lookup: {str(e)}"

def main():
    ip = input("Enter the IP address you want to get information about: ")
    info = get_ip_info(ip)
    
    print("\nDetailed IP Information:")
    print(f"  ip: {info.get('ip', 'N/A')}")
    print(f"  hostname: {info.get('hostname', 'N/A')}")
    print(f"  city: {info.get('city', 'N/A')}")
    print(f"  region: {info.get('region', 'N/A')}")
    print(f"  country: {info.get('country', 'N/A')}")
    print(f"  loc: {info.get('loc', 'N/A')}")
    print(f"  org: {info.get('org', 'N/A')}")
    print(f"  postal: {info.get('postal', 'N/A')}")
    print(f"  timezone: {info.get('timezone', 'N/A')}")
    print(f"  readme: {info.get('readme', 'N/A')}")
    
    print("\nIP Information:")
    print(f"IP: {info.get('ip', 'N/A')}")
    print(f"City: {info.get('city', 'N/A')}")
    print(f"Region: {info.get('region', 'N/A')}")
    print(f"Country: {info.get('country', 'N/A')}")
    print(f"Location: {info.get('loc', 'N/A')}")
    print(f"ISP: {info.get('org', 'N/A')}")
    
    print("\nPerforming WHOIS lookup...")
    whois_info = whois_lookup(ip)
    print(whois_info)
    
    print("\nPerforming DNS lookup...")
    dns_info = dns_lookup(ip)
    print(dns_info)
    
    # Pause until a key is pressed
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
