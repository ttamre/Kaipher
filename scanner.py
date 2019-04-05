#!/usr/bin/env python3

"""
Kaipher
Copyright (C) 2019 Tem Tamre

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

Filename: scanner.py
Description: Port and idle scanners

Sources used
https://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python/
"""

import crayons
import os
import socket
import subprocess
import sys
import time

CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"
TITLE = """
██╗  ██╗ █████╗ ██╗██████╗ ██╗  ██╗███████╗██████╗ 
██║ ██╔╝██╔══██╗██║██╔══██╗██║  ██║██╔════╝██╔══██╗
█████╔╝ ███████║██║██████╔╝███████║█████╗  ██████╔╝
██╔═██╗ ██╔══██║██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
██║  ██╗██║  ██║██║██║     ██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""


def port_scan(address, full_scan):
    """
    Execute a port scan on the given address
    Parameter(s):   address:String  Address to scan
    Return:         None
    """

    # Clear screen and print title
    subprocess.call(CLEAR_COMMAND, shell=True)
    print(crayons.red(TITLE))
    

    # Get the correct IP version
    if is_ipv6(address):
        ip_version = socket.AF_INET6
    else:
        ip_version = socket.AF_INET
    
    # Get the IP address of the host and print it
    remoteServerIP = socket.getaddrinfo(address, None, ip_version)[0][-1][0] # socket.getaddrinfo() return a structure like [[a,b,c,(d,e)]]
    print("Performing port scan on remote host: {}\n".format(crayons.green(remoteServerIP, bold=True)))

    # Scan all ports from 1 to 1024 and time it
    start = time.time()
    try:
        ports_to_scan = range(1,63336) if full_scan else range(1,1025)
        for port in ports_to_scan:
            sock = socket.socket(ip_version, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))

            if result == 0:
                print("Port {}:\t{}".format(str(port).zfill(2), crayons.green("OPEN", bold=True)))
            
            sock.close()

    except KeyboardInterrupt:
        print("\nKeyboard interrupt. Exiting...")
        sys.exit()
    except socket.gaierror:
        print("Hostname could not be resolved. Exiting...")
        sys.exit()
    except socket.error:
        print("Couldn't connect to server. Exiting...")
        sys.exit()

    # Print elapsed time
    elapsed = time.time() - start
    elapsed = time.strftime("%H:%M:%S", time.gmtime(elapsed))
    print("\nScanning completed in {}\n".format(crayons.blue(elapsed)))


def idle_scan(address, full_scan):
    """
    Execute an idle scan on the given address
    Parameter(s):   address:String  Address to scan
    Return:         None
    """

    # Clear screen and send title and target address to terminal
    subprocess.call('clear', shell=True)
    print(crayons.red(TITLE))
    remoteServerIP = socket.gethostbyname(address)

    print("Performing idle scan on remote host: {}\n".format(crayons.green(remoteServerIP, bold=True)))


def is_ipv6(address):
    """
    Check if the given address is a valid IPv6 address
    Parameter(s):   address:String  Address to check
    Return:         True if address is a valid IPv6 address, false otherwise
    """
    try:
        socket.inet_pton(socket.AF_INET6, address)
        return True
    except OSError:
        return False