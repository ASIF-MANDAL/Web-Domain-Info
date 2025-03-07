import pandas as pd
import socket
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

# Function to get IP address, IP class, and reply status
def get_domain_info(domain):
    try:
        # Get IP address
        ip_address = socket.gethostbyname(domain)
        
        # Determine IP class
        first_octet = int(ip_address.split('.')[0])
        if first_octet <= 127:
            ip_class = 'A'
        elif first_octet <= 191:
            ip_class = 'B'
        elif first_octet <= 223:
            ip_class = 'C'
        elif first_octet <= 239:
            ip_class = 'D'
        else:
            ip_class = 'E'
        
        # Check if the website is reachable
        try:
            response = requests.get(f"http://{domain}", timeout=5)
            reply = "Reachable" if response.status_code == 200 else "Unreachable"
        except:
            reply = "Unreachable"
        
        return {
            'Domain Name': domain,
            'IP Address': ip_address,
            'IP Class': ip_class,
            'Reply': reply
        }
    except socket.gaierror:
        return {
            'Domain Name': domain,
            'IP Address': 'N/A',
            'IP Class': 'N/A',
            'Reply': 'Unreachable'
        }

# Read domains from websites.txt
with open("websites.txt", "r") as file:
    domains = [line.strip() for line in file.readlines()]

# Use ThreadPoolExecutor to speed up the process
results = []
with ThreadPoolExecutor(max_workers=50) as executor:
    future_to_domain = {executor.submit(get_domain_info, domain): domain for domain in domains}
    for future in as_completed(future_to_domain):
        results.append(future.result())

# Create a DataFrame
df = pd.DataFrame(results)

# Save to Excel
df.to_excel("domain_info.xlsx", index=False)

print("Excel file 'domain_info.xlsx' has been created.")