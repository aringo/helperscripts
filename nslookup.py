#!/usr/bin/env python3 
import sys
import argparse
import ipaddress 
import subprocess

def nslookup(q,ip,ipfile): 
    resolved_ip = None    
    process = subprocess.Popen(["nslookup", q], stdout=subprocess.PIPE)
    output, error = process.communicate()
    output = output.decode().split('\n')

    if ip == True:
        for data in output:
            if 'name' in data:
                hostname = data.split("name = ")[-1].rstrip(".")
                print(hostname)
        return  
    else:
        resolved_ip = output[-3].split("Address: ")[-1]
        
    if ipfile:
        if resolved_ip in ipfile:
            print(q)
    else:
        print(resolved_ip)



def main(args):
    query = args.query

    if args.ipfile:
        with open(args.ipfile,'r') as readhandle:
            ipfile = readhandle.read()
    else:
        ipfile = None

    for q in query:
        ip = True
        try:
            ipaddress.IPv4Address(q)
        except:
            ip = False
        
        nslookup(q,ip,ipfile)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="nslookup wrapper")
    parser.add_argument(action="store",dest="query",nargs='+',help="what to lookup")
    parser.add_argument("-f",action="store",dest="ipfile",help="file to reference")
    args = parser.parse_args()
    main(args)
