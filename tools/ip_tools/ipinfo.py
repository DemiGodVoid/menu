import requests
import whois
import socket

def get_ip_info(ip):
    url = f"https://ipinfo.io/{ip}/json"
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Error: Unable to fetch data (status code: {response.status_code})")
        return {}

def get_whois_info(domain):
    try:
        w = whois.whois(domain)
        return w
    except Exception as e:
        print(f"Error: Unable to fetch WHOIS data ({str(e)})")
        return {}

def get_dns_info(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror:
        print(f"Error: Unable to resolve DNS for {domain}")
        return "N/A"

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

    if 'hostname' in info and info['hostname'] != 'N/A':
        domain = info['hostname']
        print(f"\nPerforming WHOIS lookup for {domain}...")
        whois_info = get_whois_info(domain)
        print("\nWHOIS Information:")
        for key, value in whois_info.items():
            print(f"  {key}: {value}")

        print(f"\nPerforming DNS lookup for {domain}...")
        dns_info = get_dns_info(domain)
        print(f"\nDNS Information:")
        print(f"  Domain: {domain}")
        print(f"  IP Address: {dns_info}")
    
    # Pause until a key is pressed
    input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
