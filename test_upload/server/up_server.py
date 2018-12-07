#!/usr/bin/env python3

import socket
import sys
import base64
import json

BEAGLEIP = '192.168.6.2' # endereço da beagl bone
LOOPIP = '127.0.0.1'

def send_byte(myconn):
	# recv()
	data = myconn.recv(1024)
	print("[RECV]: " + str(data))
	if not data:
		return 'BREAK'
	
	# send()
	myconn.sendall(b"[SERVER] " + data)

def save_file(myconn):
	# recv()
	data = myconn.recv(1024)
	print("[RECV]: " + str(data))
	if not data:
		return 'BREAK'

	# save file
	f = open('mytest.txt', 'w')
	f.write(data.decode())
	f.close()
	
	# send()
	myconn.sendall(b"[SERVER] saved \"mytest.txt\" file")

def conn_server(host, port, max_user):
	# socket()
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		print("socket created. " + str(type(s)))

		# bind()
		s.bind((host, port))
		print("socket binded. " + str((host, port)))

		# listen()
		s.listen(MAX_USER)
		print("socket listenning to " + str(max_user) + " users.")

		# accept()
		conn, addr = s.accept()
		print("socket accepted connection. conn: " + str(type(conn)) + "; addr: " + str((addr)))

		with conn:
			print("[WITH] conn... " + str(type(conn)))

			while True:
				if 'BREAK' == save_file(conn):
					break

	print("connection closed.")


if __name__ == "__main__":

	# Definindo endereço do IP do servidor e porta
	HOST = ''
	PORT = 1234
	MAX_USER = 3

	conn_server(HOST, PORT, MAX_USER)
	print('exit')