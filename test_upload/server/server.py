#!/usr/bin/env python3

import socket
import sys
import base64
import json
import time

BEAGLEIP = '192.168.6.2' # endereço da beagl bone
LOOPIP = '127.0.0.1'


# deserializes json from file into a dict(?)
#json_o = (json.load(f))


def save_file(filename, content):
	# saving file
	f = open('mytest.txt', 'w')
	f.write(content.decode())
	f.close()
	
	return True

def conn_server(host, port, max_user):
	# socket()
	serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	print("socket created. " + str(type(serversocket)))

	# bind()
	serversocket.bind((host, port))
	print("socket binded. " + str((host, port)))

	# listen()
	serversocket.listen(MAX_USER)
	print("socket listenning to " + str(max_user) + " users.")

	# accept()
	conn, addr = serversocket.accept()
	print("socket accepted connection. conn: " + str(type(conn)) + "; addr: " + str((addr)))

	try:
		print("[WITH] conn... " + str(type(conn)))

		command = ''
		recv_iterations = 4
		while command != 'EXIT':
			# recv()
			data = conn.recv(1024)
			print('data: ' + data.decode())
			time.sleep(1)
			
			if not data:
				break
			#DEBUG
			print('deserealizing recieved data...')
			# treat byte data as json
			time.sleep(1)
			print ("\tdata type: " + str(type(data)))
			print(data)
			json_response = json.loads(data.decode())

			# treat payload
			#if json_response['OP'] == 'SEND_FILE':
			#	print(save_file(json_response['BODY']['filename'],
			#								json_response['BODY']['content']))
	except Exception as e:
	    exc_type, exc_obj, exc_tb = sys.exc_info()
	    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
	    print(exc_type, fname, exc_tb.tb_lineno)
	finally:
		conn.close()
		serversocket.close()
		print("connection closed.")


if __name__ == "__main__":

	# Definindo endereço do IP do servidor e porta
	HOST = ''
	PORT = 1234
	MAX_USER = 3

	conn_server(HOST, PORT, MAX_USER)
	print('exit')