#!/usr/bin/python
import os.path
import socket, subprocess

def get_ip_address(hostname):
    return socket.gethostbyname(hostname)
    
def get_hostname():
    hostname = socket.gethostname()
    domain = os.path.splitext(hostname)[1]

    if(domain != '.local'):
        hostname += ".local"
    return hostname
    
def main():
    hostname = get_hostname()
    ip_address = get_ip_address(hostname)
    
    #print ip_address, type(ip_address)
    
    if ip_address == '127.0.0.1':
        print "Are you connect to the network?"
    else:
        print "IPv4: " + ip_address
    
if __name__ == '__main__':
    main()
