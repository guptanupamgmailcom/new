#!/usr/bin/python3
"""
# Scanning single port
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

host = input("Please enter the IP you want to scan: ")
port = int(input("Please enter the port you want to scan: "))


def portScanner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

portScanner(port)"""

#Scanning multiple ports
import socket

target = 'localhost' # replace with the IP or hostname of the target machine
ports = [21, 22, 80, 443] # replace with the list of ports to scan

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(1) # set the timeout for the connection
    result = sock.connect_ex((target, port)) # attempt to connect to the port
    if result == 0:
        print(f"Port {port} is open")
    else:
        print(f"Port {port} is closed")

    sock.close()