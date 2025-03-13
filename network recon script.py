import socket # used in this script for the purpose of DNS lookup
import os # Library to helpm execute system commands

# Function to get the IP address of a domain
def get_ip(domain):
    ip = socket.gethostbyname(domain) # Retrieving the ip address of the entered domain name
    print(f"The IP address of {domain} is {ip}")
    return ip

# Function to perform a ping text
def ping_ip(ip):
    print(f"Pinging {ip}...")
    os.system(f"ping -n 4 {ip}")  # Ping the IP 4 times (Windows) for Linux or macOS use -c instead of -n

# Traceroute on linux and tracert on Windows for the IP
def tracert_ip(ip):
    print(f"Performing tracert to {ip}...")
    os.system(f"tracert {ip}")  # Run tracert on the IP (Windows)

# Functio to perform WHOIS query to get information about the domain
def whois_query(domain):
    print(f"WHOIS information for {domain}:")
    os.system(f"whois {domain}")

# Domain to scan
domain = input("Pease enter domain name: ")


# Performing basic reconnaissance and calling on each function already created
ip_address = get_ip(domain)

ping_ip(ip_address)

tracert_ip(ip_address)

whois_query(domain)






