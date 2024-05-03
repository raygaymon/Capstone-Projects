# using sockets method

# with help of some reference material

import socket
import re

# use re to identify ip address and socket range in user input
ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

# identify port number from input <port>-<port>
port_pattern = re.compile(r"^([0-9]+)-([0-9]+)")

# array to store open ports
open_ports = []
closed_ports = []

# get user input of ip address
def get_user_ip():
    while True:
        ip = input("Please enter the IP address you would like to scan: ")
        m = re.search(ip_pattern, ip)
        if m:
            print(f"{m.group()} is a valid IP address.")
            return ip
        else:
            print(f"{ip} is not a valid ip address.")

# get user input for ports to scan
def get_user_ports():
    while True:
        ports = input("Please enter the ports you weould like to scan in this format (port)-(port): ")
        res = re.search(port_pattern, ports)
        if res:
            print(f"{res.group(1)} - {res.group(2)} is a valid port range")
            return (res.group(1), res.group(2))
        else:
            print("Input is not valid.")

# scan port method
def scan_port(port_min, port_max, ip):

    # scan every port in given range
    for i in range(port_min, port_max+1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.settimeout(0.5)
                s.connect((ip, i))
                # if connection is successful append port number to open_port list
                open_ports.append(i)
            except:

                # connection threw an error and we append to closed port list for visibility
                closed_ports.append(i)

def main():
    ip_to_scan = get_user_ip()
    port_min, port_max = get_user_ports()
    scan_port(int(port_min), int(port_max), ip_to_scan)

    for o in open_ports:
        print(f"Port {o} is an open port.")
    for c in closed_ports:
        print(f"Port {c} is closed.")

if __name__ == "__main__":
    main()

# 192.168.1.9