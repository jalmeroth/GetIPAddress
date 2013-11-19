#!/usr/bin/python
import socket, subprocess

def get_ip_address():
    return socket.gethostbyname(socket.gethostname())
    
def get_hostname():
    return socket.gethostname()

def display(dialog):
    output = subprocess.check_output(['osascript', '-e', dialog])
    return output

def main():
    host_name = get_hostname()
    ip_address = get_ip_address()

    print host_name + ': ' + ip_address
    
    if(ip_address == "127.0.0.1"):
        dialog = 'tell application "System Events" to display dialog "Steck ihn rein, Diggah!" buttons ("OK") default button "OK"'
        print display(dialog)
    else:
        dialog = 'tell application "System Events" to display dialog "IPv4: ' + ip_address + ' " buttons ("OK") default button "OK"'
        print display(dialog)
    
    
if __name__ == '__main__':
    main();