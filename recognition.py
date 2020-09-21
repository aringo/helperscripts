#!/usr/bin/env python3

import json                                                              # parsing responses
import requests
import argparse                                                          
from requests.packages.urllib3.exceptions import InsecureRequestWarning  # stops insecure ssl cert warning 
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def main(args):
    
    # query since
    epoch_start_time = args.epoch_start_time
    query_amount = args.query_amount

    if args.bearer:
        bearer = args.bearer 
    else:
        try: 
            with open("/tmp/synacktoken","r") as f:
                bearer = f.read()
        except:
            bearer = input("An access_token is needed: ")   

    synack_headers = {"Connection": "close", 
                      "Authorization": "Bearer "+f"{bearer}", 
                      "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/604.3.5 (KHTML, like Gecko) Version/11.0.1 Safari/604.3.5", 
                      "Accept": "*/*", 
                      "Sec-Fetch-Site": "same-origin", 
                      "Sec-Fetch-Mode": "cors", 
                      "Sec-Fetch-Dest": "empty", 
                      "Referer": "https://platform.synack.com/transactions",
                      "Accept-Encoding": "gzip, deflate"}
    trans_url = f"https://platform.synack.com/api/transactions?page=1&per_page={query_amount}"           
    try:
        monies = 0
        patch_count = 0 
        vuln_count = 0 
        missions = 0
        data = requests.get(trans_url, headers=synack_headers, verify=False).json()
    

        if len(data) > 0:
            for i in range (len(data)):        
                
                transaction = dict(data[i])
                title = transaction["title"]
                tamount = transaction["amount"]
                ttype = transaction["reference_type"]
                tcdate = transaction["created_at"]  
                if tcdate > epoch_start_time:	

                    if ttype == "PatchVerification":
                        patch_count += 1
                        monies += float(tamount)

                    elif ttype == "Vulnerability":       
                        vuln_count += 1 
                        monies += float(tamount)

                    elif ttype == "Task":
                        missions += 1
                        monies += float(tamount)

        print(f"\nAmount of funds: {monies}")
        print(f"Patch Verifications: {patch_count}")
        print(f"Vuln count: {vuln_count}")
        print(f"Missions count: {missions}")
        print(f"Recognition Points: {vuln_count + (missions//20)}\n")
    
    except:
        print("I dunno ")            
      

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Script for Tracking Recognition - Swiggity swooty coming for that hoodie")
    parser.add_argument("-a",action="store",dest="bearer",help="Auth Token")
    parser.add_argument("-t",action="store",dest="epoch_start_time",type=int,help="Query Since Epoch",default=1593561600)
    parser.add_argument("-q",action="store",dest="query_amount",help="Amount of Transaction",default=500)
    
 
    args = parser.parse_args()
    main(args)
