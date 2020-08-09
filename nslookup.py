#!/usr/bin/env python3 
import sys
import argparse
import ipaddress 
import subprocess

def main(args):
    query = args.query

    def nslookup(q,ip): 
        process = subprocess.Popen(["nslookup", q], stdout=subprocess.PIPE)
        output, error = process.communicate()
        output = output.decode().split('\n')

        if ip == True:
            for data in output:
                if 'name' in data:
                    hostname = data.split("name = ")[-1].rstrip(".")
                    print(hostname)
        else:
            print(output[-3].split("Address: ")[-1]) 

    for q in query:
        ip = True
        try:
            ipaddress.IPv4Address(q)
        except:
            ip = False
        
        nslookup(q,ip)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="nslookup wrapper")
    parser.add_argument(action="store",dest="query",nargs='+',help="what to lookup")
    args = parser.parse_args()
    main(args)
