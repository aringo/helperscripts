#!/usr/bin/env python3

# kept having scope that was a mix of public and private IPs
# cat scope.txt | ./get_public.py | tee -a public  

import sys
from ipaddress import ip_address

for line in sys.stdin:
    try:
        if ip_address(line.rstrip('\n')).is_private != True:
            sys.stdout.write(line)
    except:
        pass
