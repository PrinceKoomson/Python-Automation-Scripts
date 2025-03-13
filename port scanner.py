import socket #create a socket object and perform network operations.

# Function to scan port which takes two parameters(ip and port)
def scan_port(ip, port):

    # Try block handling used to handle predictable and unpredictable errors
    try:
        # Creating a new socket object
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # socket object taking in IPv4 addresses(AF_INET) and utilizing TCP(SOCK_STREAM) instead of UDP

        socket.setdefaulttimeout(1)  # Set timeout for the connection which is established

        result = sock.connect_ex((ip, port))  # Attempting to connect to specified port for the ip address using connect_ex and storing outcome(error code) in result



#If statement checks the error stored in results and if it's equal to zero prints out formatted string indicating it's opened or else it's closed

        if result == 0:
            print(f"Port {port} is open on {ip}")
        else:
            print(f"Port {port} is closed on {ip}")
        sock.close()  # Close the socket connection

    except socket.error as error: # code handling any unforseen errors
        print(f"Error scanning port {port}: {error}")


# Function to generate ip address from given domain
def get_ip(domain):
    ip = socket.gethostbyname(domain) # Generating ip address using gethostbyname provided by socket
    print(f"The IP address of {domain} is {ip}")
    return ip

# List of common ports to scan
ports = [22, 80, 443, 8080]

# Domain name to scan
domain = input("Please enter a domain name: ")
ip_address = get_ip(domain)

print(f"Scanning {ip_address}...")
for port in ports: # This line starts a for loop that iterates over the list of ports to scan.

# This line calls the scan_port function for each port in the list, passing the IP address and port number as arguments.
    scan_port(ip_address, port)