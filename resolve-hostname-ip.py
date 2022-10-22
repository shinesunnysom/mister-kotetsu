#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Credits: Suresh Vina
"""

import socket

with open(r'directory name input.txt', 'r') as r_file:
    with open(r'directory name output.txt', 'w') as w_file:
        for hostname in r_file.readlines():
            hostname = hostname.strip()
            try:
                print('Resolving : ' + hostname)
                ip = socket.gethostbyname(hostname)
                w_file.write(hostname + ' - ' + ip + '\n')
            except:
                print('Unable to resolve: ' + hostname)
