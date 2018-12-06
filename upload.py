#!/usr/bin/env python3

import socket
import sys

SERVER = '192.168.6.2'
PORT = 1234

s = socket.socket()
s.connect((SERVER, PORT))
f = open('img.png', 'rb')
l = f.read(1024)
while (l):
    s.send(l)
    l = f.read(1024)
s.close()
f.close()
