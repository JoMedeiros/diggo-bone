#!/usr/bin/env python3

import socket
import sys
import base64
import json

SERVER = socket.gethostname() #'192.168.6.2' # endereco da beagle bone
PORT = 12345

def upload(fname, fpath='.'):
    f = open(fname, 'rb')
    s = socket.socket()
    s.connect((SERVER, PORT))
    s.send(b'SEND')
    answer = s.recv(8)# Receive confirmation to send
    print(answer.decode())
    s.send((fpath + '/' + fname.split('/')[-1]).encode())
    answer = s.recv(8)# Receive confirmation of file created
    print(answer.decode())
    l = f.read(1024)
    while (l):
        s.send(l)
        l = f.read(1024)
    s.close()
    f.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('digite um nome para o arquivo')
        sys.exit()
    fname = sys.argv[1]
    upload(fname)
 
