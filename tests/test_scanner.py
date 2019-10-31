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

Filename: test_scanner.py
Description: Test class for the scanner file
"""

import unittest
import socket

import scanner

class TestKaipher(unittest.TestCase):
    def test_port_scan_full(self):
        address = socket.gethostbyname(socket.gethostname())
        full_scan = True
        port_number = 80
        
        try:
            scanner.port_scan(address=address, full_scan=full_scan, port_number=port_number)
        except socket.gaierror:
            print("TestKaipher.test_port_scan_full() failed due to external environmental reasons")
            return
        except socket.error:
            print("TestKaipher.test_port_scan_full() failed due to external environmental reasons")
            return

    def test_port_scan_partial(self):
        address = socket.gethostbyname(socket.gethostname())
        full_scan = False
        port_number = 40068
        
        try:
            scanner.port_scan(address=address, full_scan=full_scan, port_number=port_number)
        except socket.gaierror:
            print("TestKaipher.test_port_scan_full() failed due to external environmental reasons")
            return
        except socket.error:
            print("TestKaipher.test_port_scan_full() failed due to external environmental reasons")
            return


    def test_idle_scan(self):
        address = None
        full_scan = None
        port_number = None
        assert scanner.idle_scan(address=address, full_scan=full_scan, port_number=port_number)

    def test_is_ipv5_true(self):
        addresses = [
            "2001:0db8:85a3:0000:0000:8a2e:0370:7334",
            "2001:db8:85a3::8a2e:370:7334"
        ]
        for ip in addresses:
            assert scanner.is_ipv6(ip)
    
    def test_is_ipv6_false(self):
        addresses = [
            "127.0.0.1",
            "127001",
            "ipv4 address",
            127001,
            127.001,
            None
        ]
        for ip in addresses:
            assert not scanner.is_ipv6(ip)