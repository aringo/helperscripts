"""
I like my ipv4s one by one and so do most tools
cat jackedtargets | uncidr.py > targets 
"""
#!/usr/bin/env python3

import sys
import ipaddress 

if len(sys.argv) < 2:
    commands = sys.stdin.readlines()
else:
    commands = sys.argv
for arg in commands:
    try:
        for ip in ipaddress.IPv4Network(arg.rstrip('\n')):
            print(ip)
    except:
        pass
