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
	
	return b'[SERVER] all good.'

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

		try:
			with conn:
				print("[WITH] conn... " + str(type(conn)))

				command = ''

				while command != 'EXIT':
					# recv()
					data = b''
					while True:
						parcial_data = conn.recv(8)
						print("[RECV]: " + parcial_data.decode())
						if not parcial_data: 
							break
						data += parcial_data
						#DEBUG
						print('data: ' + data.decode())
						#time.sleep(.5)

					#DEBUG
					print('Treating recv.')
					# treat byte data as json
					print ("data type: " + str(type(data)))
					json_response = json.loads(data.decode())

					# get operation
					if json_response['OP'] == 'SEND_FILE':
						save_file(json_response['BODY']['filename'],
							json_response['BODY']['content'])
					else:
						print('fudeu tudo')
						break
		except Exception:
			#print("I/O error({0}): {1}".format(errno, strerror))
			tb = sys.exc_info()
			print(str(tb))
		finally:
			s.close()

	print("connection closed.")


if __name__ == "__main__":

	# Definindo endereço do IP do servidor e porta
	HOST = ''
	PORT = 1234
	MAX_USER = 3

	conn_server(HOST, PORT, MAX_USER)
	print('exit')