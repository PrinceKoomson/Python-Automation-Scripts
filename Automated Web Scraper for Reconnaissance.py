# Python Script to authomate web scrapper for reconnaissance


import requests  # Request library is used to send HTTP request to a specified URL and handles responces.
from bs4 import BeautifulSoup # BeatifulSoup from bs4(BeutifulSoup 4) is used for parsing HTML and XML documents. Help un also extracting HTML tags.

# Function to scrape a domain and extract subdomains from site
def scrape_website(domain):  
    response = requests.get(domain) # Sends a get request to domain name provided and stores it in response
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extracting  and printing all links associated with domain
    result = [] # Creating an empty list

    # for loop iterate over all anchor tags <a> and retrieves all tags that have href to the true.
    for link in soup.find_all('a', href=True):
        if "http" in link['href']:   # checks if http string is within the items stored in the list
            result.append(f"Found URL: {link['href']}")
    
    return result

# Taking user input and adding needed prefix to generate a url
domain = input(" Please enter the domain name: ")
prefix = "https://www."

url = f'{prefix}{domain}'

# Run the web scraping function
result = scrape_website(url)

# Store the resulting list in a file.
with open(f'{domain}.txt', "w+") as file:
    for item in  result:
        file.write(f'{item}\n')
