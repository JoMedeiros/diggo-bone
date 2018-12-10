#!/usr/bin/env python3

import socket
import json
import time

# user defined modules
#import calc_diff
import diggo_socket as ds

MAXBUFF = 1024
MAXUSERS = 1
HOST = ''
PORT = 9999

SKCT_MAN = ''

# TODO : implementar e testar 'SYNC' [PRIORIDADE].
# TODO : comunicação server/client em cada caso.
def treat_client_request(request):
	"""
	gera eenvia um payload para ser enviado ao cliente dado um request
	"""

	global SKCT_MAN

	# gera dicionario dado o request
	request = json.loads(request)

	if request['OP'] == 'SYNC':
		# sincroniza server com client
		# 	calcula tree sincronizada
		#	aplica correções no diretorio atual com a sync_tree
		#	envia a sync_tree para o client
		pass

	if request['OP'] == 'RESET_SERVER':
		# resetar servidor
		# 	deleta tudo do servidor
		#	last_sync_tree do servidor passa passa as ser uma tree vazia
		#   REVIEW : envia resposta para o cliente
		pass

	if request['OP'] == "GET_SERVER_FILELIST":
		# a lista de arquivos atualmente no server foi requisitada.
		# 	envia resposta com lista.
		# 	REVIEW : retorna resposta
		pass

	if request['OP'] == "TEST":
		pass

	if request['OP'] == "QUIT":
		print("\t sending payload...")
		p , p_size = SKCT_MAN.ready_payload({ "OP": "QUIT", "BODY": "I am server testing."})
		print("\t sending payload...")
		SKCT_MAN.send_payload(p, p_size)
		print("\t done sending payload...")
		return 'QUIT'

	pass


# TODO : testar
def create_server_socket():
	"""
	admnistra o socket do servidor.
	"""

	global MAXUSERS
	global HOST
	global PORT

	global SKCT_MAN
	
	# creating socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((HOST,PORT))
	sock.listen(MAXUSERS)
	print("socket on.")

	# accepting connection
	conn, addr = sock.accept()
	print("connection on.")

	SKCT_MAN = ds.Diggo_socket_manager(conn, 'SERVER')

	# connection loop
	while True:

		# TODO : retirar prints desnecessários

		# recv() treat client request
		request = SKCT_MAN.recv_payload()
		# TEST
		print("")
		answer = treat_client_request(request)
		if answer == 'QUIT':
			break
		# treat_client_request(client_response)

		print("")

	print('closing connection...')
	conn.close()
	print('closing server...')
	sock.close()

if __name__ == "__main__":
	create_server_socket()
	print('Exiting...')