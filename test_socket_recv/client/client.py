#!/usr/bin/env python3

import socket
import json

def ready_file(filename):
	f = open(filename, 'r')
	content = f.read()

	# jsoning
	payload = {"filename": filename, "content": content}
	payload = json.dumps(payload)
	buffsize = len(payload)

	return payload, buffsize

def socket_conn_client():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect(("127.0.0.1", 9999))

	while True:
		
		# 1st ROUND

		comm = input("> comm: ")
		
		if comm == 'quit':
			sock.send(comm.encode())
			break
		
		buffcontent, buffsize = ready_file('test.txt')
		
		print("\tsending buffsize of:" + str(buffsize))
		# send() buffsize
		sock.send(str(buffsize).encode())

		# recv() buffsize
		print(sock.recv(1024).decode())


		# 2nd ROUND

		# send() content
		print("\tsending content:" + buffcontent[10])
		sock.send(buffcontent.encode())

		# recv() message
		print(sock.recv(1024).decode())

		print("")

	sock.close()

if __name__ == "__main__":
	socket_conn_client()
	print('Exiting...')