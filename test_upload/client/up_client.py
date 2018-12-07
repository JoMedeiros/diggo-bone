#!/usr/bin/env python3

import socket
import sys
import base64
import json

#for testing
import time

#self
import user_comm

BEAGLEIP = '192.168.6.2' # endereço da beagle bone
LOOPIP = '127.0.0.1'

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
		user_comm.user_loop(s)

	print("connection closed.")


if __name__ == "__main__":

	# Definindo endereço do IP do servidor e porta
	SERVER = LOOPIP
	PORT = 1234 
	MESSAGE = b'default'
	SERVER_MODE = 'LOOPBACK'
	FILENAME = 'test.txt'

	if len(sys.argv) == 2:
		if sys.argv[1] == 'b': # utilizando com a beagle de server
			SERVER = BEAGLEIP

	# conectar com o usuário
	conn_user(SERVER, PORT, MESSAGE, FILENAME)
	print('exit')