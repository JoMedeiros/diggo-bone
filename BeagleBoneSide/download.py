#!/usr/bin/env python3

import socket
import sys
import base64
import json

SERVER = socket.gethostname() #'192.168.6.2' # endereco da beagle bone
PORT = 12345

def download():
    s = socket.socket()
    s.bind((SERVER, PORT))
    s.listen(5)
    c, addr = s.accept()
    request = c.recv(16)
    print('Operation: ' + request.decode())
    c.send(b'OK') # Send confirmation
    fpath = c.recv(1024).decode() # Receive the file name
    print('File name: '+fpath.decode())
    f = open(fpath, 'w+')
    c.send(b'NAMED')
    #print(answer.decode())
    #s.send(fpath.split('/')[-1].encode())
    #answer = s.recv(8)# Receive confirmation of file created
    #print(answer.decode())
    l = c.recv(1024)
    while (l):
        f.write(l)
        l = c.recv(1024)
    c.close()
    f.close()

if __name__ == "__main__":
    download()
 
