#!/usr/bin/env python3

import socket
import sys
import base64
import json

#for testing
import time

BEAGLEIP = '192.168.6.2' # endereço da beagle bone
LOOPIP = '127.0.0.1'

def send_file(mysocket, filename):
	f = open(filename,'r')
	mysocket.sendall(f.read().encode())
	f.close()

# test
def send_message(mysocket, message):
	s.sendall(message)


def conn_user(server, port, message, filename):

	# socket()
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		
		# connect()
		s.connect((server, port))
		print("socket connected to. " + str((server, port)))

		# send()
		#s.sendall(message)

		send_file(s, filename)

		# recv()
		data = s.recv(1024)
		if data == '':
			print(data)

	print("connection closed.")


if __name__ == "__main__":

	# Definindo endereço do IP do servidor e porta
	SERVER = LOOPIP
	PORT = 1234 
	MESSAGE = b'default'
	SERVER_MODE = 'LOOPBACK'
	FILENAME = 'user_comm.py'

	if len(sys.argv) == 2:
		if sys.argv[1] == 'b': # utilizando com a beagle de server
			SERVER = BEAGLEIP

	conn_user(SERVER, PORT, MESSAGE, FILENAME)
	print('exit')