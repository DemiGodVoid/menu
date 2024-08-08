import requests

def get_ip_info(ip):
    url = f"https://api.ipapi.com/{ip}?access_key=YOUR_ACCESS_KEY"
    response = requests.get(url)
    data = response.json()
    return data

def main():
    ip = input("Enter the IP address you want to get information about: ")
    info = get_ip_info(ip)
    
    print("\nIP Information:")
    print(f"IP: {info.get('ip', 'N/A')}")
    print(f"City: {info.get('city', 'N/A')}")
    print(f"Region: {info.get('region_name', 'N/A')}")
    print(f"Country: {info.get('country_name', 'N/A')}")
    print(f"Location: {info.get('latitude', 'N/A')}, {info.get('longitude', 'N/A')}")
    print(f"ISP: {info.get('org', 'N/A')}")

if __name__ == "__main__":
    main()
