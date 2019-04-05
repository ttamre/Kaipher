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

Filename: Kaipher.py
Description: Main menu for the kaipher program

Sources used
https://www.pythonforbeginners.com/code-snippets-source-code/port-scanner-in-python/

Current structure
    - Everything contained in kaipher.py

Extended structure
    - Main file: kaipher.py
    - Port and idle scanner: scanner.py
    - Extra functionality: ?.py


TODO:
    1) Port project into extended structure
    2) Learn idle scanning
    3) Implement idle scanner
    4) Brainstorm more functionality
"""

import argparse
import crayons
import os
import socket
import subprocess
import sys
import time

__author__  = "Tem Tamre"
__license__ = "GNU GPLv3"
__version__ = "1.0"
__status__  = "Dev"

CLEAR_COMMAND = "cls" if os.name == "nt" else "clear"
TITLE = """
██╗  ██╗ █████╗ ██╗██████╗ ██╗  ██╗███████╗██████╗ 
██║ ██╔╝██╔══██╗██║██╔══██╗██║  ██║██╔════╝██╔══██╗
█████╔╝ ███████║██║██████╔╝███████║█████╗  ██████╔╝
██╔═██╗ ██╔══██║██║██╔═══╝ ██╔══██║██╔══╝  ██╔══██╗
██║  ██╗██║  ██║██║██║     ██║  ██║███████╗██║  ██║
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
"""

def main():
    args = parse_arguments()
    scan = args.idle
    scan(args.address)


def parse_arguments():
    """
    Parse command line arguments

    Parameter(s):   None
    Return:         args:argparse.Namespace     Parsed args object that contains all passed arguments
    """
    parser = argparse.ArgumentParser(prog="kaipher.py",
                                    description="Kaipher v{}, a passive network scanning tool".format(__version__),
                                    epilog="Kaipher Copyright (C) 2019 Tem Tamre.\n "
                                    "This program comes with ABSOLUTELY NO WARRANTY. "
                                    "This is free software, and you are welcome to redistribute it "
                                    "under conditions met by the {} license. This tool is intended "
                                    "to be used as a learning exercise and is not intented for illegal "
                                    "or otherwise malicious purposes. The creators and maintainers of this "
                                    "project assume no responsibility for misuse of this program\n".format(__license__))

    parser.add_argument("address",
                        nargs=1,
                        type=str,
                        help="Address to scan")

    parser.add_argument("-i", "--idle", "--idlescan",
                        action="store_const",
                        const=idle_scan,
                        default=port_scan,
                        help="Perform an idle scan instead of a standard port scan")

    args = parser.parse_args()
    args.address = args.address[0]
    return args


def port_scan(address):
    """
    Execute a port scan on the given address
    Parameter(s):   address:String  Address to scan
    Return:         None
    """

    # Clear screen and send title and target address to terminal
    subprocess.call(CLEAR_COMMAND, shell=True)
    print(crayons.red(TITLE))
    remoteServerIP = socket.gethostbyname(address)

    print("Performing port scan on remote host: {}\n".format(crayons.green(remoteServerIP, bold=True)))

    # Scan all ports from 1 to 1024 and time it
    start = time.time()

    try:
        for port in range(1,1025):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))

            if result == 0:
                print("Port {}:\t{}".format(port, crayons.green("OPEN", bold=True)))
            
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

    elapsed = time.time() - start
    elapsed = time.strftime("%H:%M:%S", time.gmtime(elapsed))

    print("\nScanning completed in {}\n".format(crayons.blue(elapsed)))


def idle_scan(address):
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

if __name__ == "__main__":
    main()