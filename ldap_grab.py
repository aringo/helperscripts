#!/usr/bin/env python3
import sys 
import time
import ldap3

# quick script for LDAP query, Replace hardcoded <FILL_WITH_OBJECT> with Object etc.

if len(sys.argv) == 1 or len(sys.argv) > 2:
    print(f"python3 {sys.argv[0]} <target>")
    sys.exit()

target = sys.argv[1]
server = ldap3.Server(target, get_info = ldap3.ALL, port=636, use_ssl=True)
connection = ldap3.Connection(server)
bind = connection.bind()
if bind == False:
    print(f"Failed to bind to {target}")
print(f"Bound to {target}")
print("Server info")
time.sleep(2)
print(server.info)
time.sleep(5)
connection.search(search_base='o=<FILL_WITH_OBJECT>', search_filter='(objectClass=*)', search_scope='SUBTREE', attributes='*')
print(connection.entries)
