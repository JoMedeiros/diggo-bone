#!/usr/bin/env python3

import socket
import sys
import base64
import json

SERVER = '192.168.6.2' # endereço da beagl bone
PORT = 1234 

s = socket.socket()
s.connect((SERVER, PORT))

if len(sys.argv) < 2:
    print('digite um nome para o arquivo')
    sys.exit()

file_json = {}
file_json['name'] = sys.argv[1]

f = open(sys.argv[1], 'rb')
#l = f.read(1024)
file_json['content'] = base64.b64encode(f.read())

#while (l):
#    s.send(l)
#    l = f.read(1024)
s.send(json.dumps(file_json))

s.close()
f.close()
