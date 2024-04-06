import requests
import sys 
import xml.etree.ElementTree as ET
from urllib.parse import urljoin
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# for dumping just HTML links from atom XML 

# get url if no arg
if len(sys.argv) > 1:
    url = sys.argv[1]
else:
    # Ask the user for the URL
    url = input("Please enter the URL: ")

# get and parse
response = requests.get(url,verify=False)
root = ET.fromstring(response.content)

# Find all 'atom:link' elements with a 'type' attribute of 'text/html'
links = root.findall(".//atom:link[@type='text/html']", namespaces={'atom': 'http://www.w3.org/2005/Atom'})

# Extract the 'href' attribute from each and print as new URLS
hrefs = [link.get('href') for link in links]

hrefs = [urljoin(url, link.get('href')) for link in links]

for href in hrefs:
    print(href)
