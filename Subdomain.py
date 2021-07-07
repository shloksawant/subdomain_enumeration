#!/bin/python3
import requests
def DomainSec():
    domain = input('Please Type Target Domain:- ')
    file = open("subdomain.txt")
    DNS = file.read()
    Subdomains = DNS.splitlines()
    for subdomain in Subdomains:
        if subdomain !=True:
            Link = f'http://{subdomain}.{domain}'
            try:
                requests.get(Link)
            except requests.ConnectionError:
                pass
            finally:
                print('[$] Your Target Subdomain :-',Link)
        else:break
DomainSec()