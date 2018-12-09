#!/usr/bin/env python3

import socket
import json

def create_server_socket():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('',9999))
	sock.listen(1)
	print(type(sock))

	conn, addr = sock.accept()
	print(str(conn), str(addr))

	while True:
		data = conn.recv(8)
		print('[CLIENT buff]: ' + str(data))

		if data.decode() == 'quit':
			break
		else:
			# got next buff size
			buffsize = int(data.decode()[:4])
			print("next buff: " + str(buffsize))

			# send()
			conn.send(b'[SERVER]: got buffsize of ' + str(buffsize).encode())

			# recv()
			data = conn.recv(buffsize)
			print('message: ' + data.decode())

			# send()
			conn.send(b'[SERVER ]: ' + data)

		print("")

	print('closing socket...')
	conn.close()			
	sock.close()

if __name__ == "__main__":
	create_server_socket()
	print('Exiting...')