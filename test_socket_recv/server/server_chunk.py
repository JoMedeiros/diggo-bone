#!/usr/bin/env python3

import socket
import json
import time

def create_server_socket():
	
	MAXBUFF = 1024

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind(('',9999))
	sock.listen(1)
	print(type(sock))

	conn, addr = sock.accept()
	print(str(conn), str(addr))

	while True:
		data = conn.recv(MAXBUFF)
		print('[CLIENT buff]: ' + str(data))

		if data.decode() == 'quit':
			break
		else:
			# got next buff size
			buffsize = int(data.decode()[:4])
			print("next buff: " + str(buffsize))

			# send() got buffsize
			conn.send(b'[SERVER]: got buffsize of ' + str(buffsize).encode())

			# recv() message loop
			data = ''
			chunks = -(-buffsize//MAXBUFF)
			for i in range(chunks):
				p_data = conn.recv(MAXBUFF)
				print('p_data: ' + p_data.decode())
				data += p_data.decode()
				time.sleep(.5)

			# send()
			conn.send(b'[SERVER ]: ' + data.encode())

		print("")

	print('closing socket...')
	conn.close()			
	sock.close()

if __name__ == "__main__":
	create_server_socket()
	print('Exiting...')