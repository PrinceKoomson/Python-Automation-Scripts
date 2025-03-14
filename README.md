﻿**Automated Web Scraper & Reconnaissance Tools**

This repository contains Python scripts designed for reconnaissance and information gathering. These tools can be used for ethical hacking, cybersecurity research, and penetration testing.

Disclaimer: These scripts are for **educational and ethical purposes only**. Unauthorized use against systems without permission is **illegal** and strictly prohibited. The author is not responsible for any misuse.

📂 Repository Contents

1. Automated Web Scraper for Reconnaissance (`Automated Web Scraper for Reconnaissance.py`)
- Description: A Python script that scrapes a website to extract subdomains and URLs.
- Usage:

  python "Automated Web Scraper for Reconnaissance.py"

- Features:
  - Takes a domain name input.
  - Uses BeautifulSoup to extract all links.
  - Saves the extracted URLs to a `.txt` file.

---

2. Network Reconnaissance Script (`network recon script.py`)
- Description: A script for performing basic reconnaissance tasks such as DNS lookup, ping tests, traceroute, and WHOIS lookups.
-Usage:
  
  python "network recon script.py"
  
-Features:
  - Retrieves the IP address of a given domain.
  - Performs a **ping** test to check connectivity.
  - Runs a **traceroute** to analyze the network path.
  - Conducts a **WHOIS lookup** to gather domain details.

---

3. Port Scanner (`port scanner.py`)
- Description: A simple Python-based port scanner to check open ports on a target domain or IP.
- Usage:

  python "port scanner.py"

-Features:
  - Takes a domain as input and resolves it to an IP address.
  - Scans common ports like **22, 80, 443, 8080**.
  - Displays open/closed port status.

---

4. SSH Brute Force Script (`SSH Brute Force Script.py`)
- Description: A script that attempts SSH login using a list of common usernames and passwords.
-Usage:
  
  python "SSH Brute Force Script.py"
  
- Features:
  - Uses **Paramiko** to establish SSH connections.
  - Tries multiple username-password combinations.
  - Reports successful or failed login attempts.

---

5. Vulnerability Scanner (`vulnerability scanner.py`)
-Description: A script that scans a target for vulnerabilities using **Nmap**.
-Usage:
  
  python "vulnerability scanner.py"
  
- Features:
  - Uses **Nmap** to perform a basic scan.
  - Executes the **`--script vuln`** Nmap command to check for known vulnerabilities.
  - Retrieves the target's IP via DNS lookup.

---

Requirements
- Python 3.x
- Required libraries (install using pip):
  
  pip install requests beautifulsoup4 paramiko
  
-Nmap must be installed on your system for the vulnerability scanner:
  -Windows: Download from [Nmap.org](https://nmap.org/download.html)
  - Linux/macOS: Install via package manager:
    
    sudo apt install nmap  # Debian/Ubuntu
    sudo yum install nmap  # CentOS
    brew install nmap      # macOS
    

---

🚀 Usage Instructions
1. Clone the repository:
   
   ```
2. Run the script of your choice by executing:

   python script_name.py
   
3. Follow the on-screen instructions to input a target domain or IP.

---


Warning: Use these tools **only on systems you have explicit permission to test**. Misuse can lead to legal consequences. Always follow ethical hacking guidelines and laws in your country.

---

🎯 **Happy Hacking! Stay Ethical!**


# Python-Automation-Scripts
