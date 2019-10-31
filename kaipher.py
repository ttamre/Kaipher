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

TODO:
    - Learn idle scanning
    - Implement idle scanner
    - Test & release v1.0
    - Brainstorm more functionality
"""

import argparse
import scanner

__author__  = "Tem Tamre"
__license__ = "GNU GPLv3"
__version__ = "1.1"
__status__  = "Dev"


def parse_arguments():
    """
    Parse command line arguments

    Parameter(s):   None
    Return:         args:argparse.Namespace     Parsed args object that contains all passed arguments
    """
    parser = argparse.ArgumentParser(prog="kaipher.py",
                                    description="Kaipher v{}, a passive port scanning tool".format(__version__),
                                    formatter_class=argparse.RawDescriptionHelpFormatter,
                                    epilog="Kaipher Copyright (C) 2019 Tem Tamre\n\n"
                                    "This program comes with ABSOLUTELY NO WARRANTY.\n"
                                    "This is free software, and you are welcome to redistribute it "
                                    "under conditions met by the {} license.\n\nThis tool is intended "
                                    "to be used as a learning exercise and is not intented for illegal "
                                    "or otherwise malicious purposes. The creators and maintainers of this "
                                    "project assume no responsibility for misuse of this program.\n".format(__license__))

    parser.add_argument("address",
                        nargs=1,
                        type=str,
                        help="address to scan")
    parser.add_argument("-i", "--idle",
                        action="store_const",
                        const=scanner.idle_scan,
                        default=scanner.port_scan,
                        help="perform an idle scan instead of a standard port scan")
    
    group = parser.add_mutually_exclusive_group(required=False)
    group.add_argument("-f", "--full",
                        action="store_true",
                        help="check all 65,335 ports instead of the first 1024")
    group.add_argument("-p", "--port",
                        type=int,
                        help="specify an individual port to check")

    args = parser.parse_args()
    args.address = args.address[0]
    return args



if __name__ == "__main__":
    args = parse_arguments()
    scan = args.idle
    print(args)
    scan(args.address, args.full, args.port)