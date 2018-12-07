#!/usr/bin/env python3

import socket
import sys
import base64
import json

# FIXME: diferenciar path de filename
def send_file(sckt, filename):

	dict_file = {'filename': filename}
	
	try:
		# lê arquivo a ser enviado
		f = open(filename,'r')

		# building json
		dict_file['content'] = f.read()
		dict_payload = {'OP': 'SEND_FILE', 'BODY':dict_file}
		# building payload
		payload = json.dumps(dict_payload).encode()
		# sending payload
		sckt.sendall(payload)

		#closing handlers
		f.close()
		
		return get_response(sckt)

	except FileNotFoundError:
		print("File not found.")
		return False

	

def get_response(sckt):
	#if skct == None:
	#print("[get_response]: no socket.")
	#pass

	data = sckt.recv(1024)
	return data.decode() == '[SERVER] all good.'
	


# Main loop for selecting type of command
def user_loop(sckt):
	# comando do usuario
	USERCOMM = ''
	COMMLIST = ["\nGET_FILELIST", "\nSEND_FILE", "\nEXIT" ]

	user_intro = "type a command: " + str(COMMLIST) + "\n>"

	while USERCOMM != 'EXIT':
		USERCOMM = input(user_intro)

		if USERCOMM == 'GET_FILELIST':
			print('Not implemented yet')
		elif USERCOMM == 'SEND_FILE':
			filename = input('enter valid filename. \n>')
			print("sending file selected....")
			response =  send_file(sckt, filename)
			print("good" if response else "bad")
		elif USERCOMM != 'EXIT':
			print('comando invalido')
		print("")

if __name__ == "__main__":
	pass