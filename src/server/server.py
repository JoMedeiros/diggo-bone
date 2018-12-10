#!/usr/bin/env python3

import socket
import json
import time

# user defined modules
#import calc_diff
import diggo_socket

MAXBUFF = 1024
MAXUSERS = 1
HOST = ''
PORT = 9999

# TODO : implementar e testar 'SYNC' [PRIORIDADE].
# TODO : comunicação server/client em cada caso.
def treat_client_request(request):
	"""
	gera eenvia um payload para ser enviado ao cliente dado um request
	"""

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

	if comm == "GET_SERVER_FILELIST":
		# a lista de arquivos atualmente no server foi requisitada.
		# 	envia resposta com lista.
		# 	REVIEW : retorna resposta
		pass
	pass


# TODO : testar
def create_server_socket():
	"""
	admnistra o socket do servidor.
	"""

	global MAXUSERS
	global HOST
	global PORT
	
	# creating socket
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.bind((HOST,PORT))
	sock.listen(MAXUSERS)
	print(type(sock))

	# accepting connection
	conn, addr = sock.accept()
	print(str(conn), str(addr))

	# connection loop
	while True:

		# TODO : retirar prints desnecessários

		# recv()
		data = conn.recv(MAXBUFF)
		print('[CLIENT buff]: ' + str(data))

		if data.decode() == 'quit':
			break
		
		# treat client request
		request = diggo_socket.recv_payload(conn, data)
		print(request)
		# treat_client_request(client_response)

		print("")

	print('closing socket...')
	conn.close()			
	sock.close()

if __name__ == "__main__":
	create_server_socket()
	print('Exiting...')