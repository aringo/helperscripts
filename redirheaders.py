#!/usr/bin/env python3
# Checks for address redirection, requests a page
# and prints what address is returned after all 
# redirection attempts from the server.  
# shows proof of forced/https redirection
# and gets end headers 

import requests

#  I just hardcode any domains I want before running it
domainlist = ["domain1", "domain2", "domain3"]

query_results = ""

for domain in domainlist:
    query_results += f"\033[1;32;49m Original domain\t{domain} \n"
    try:
        response = requests.get(domain, verify=False )
        query_results += f"\t\033[1;31;49m End address:\t{response.url}\n\n" 
        query_results += f"\t\033[1;31;49m Returned Headers:\t\n\n"
        for key, value in response.headers.items():
            query_results += f"\t\033[1;31;49m \t{key}: {value}\n\n"
    except:
         query_results += "\t\t\tFailed request\n\n"

#print("\n\n\033[1;32;49m\t\t---Results Are---\n\n")
print(query_results)
print (u"\u001b[0m")
