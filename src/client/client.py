#!/usr/bin/env python3

import socket
import json
import time

# user defined modules
#import calc_diff
import diggo_socket

MAXBUFF = 1024
SERVER_IP = "127.0.0.1"
PORT = 9999

# TODO : implementar e testar 'SYNC' [PRIORIDADE].
def user_operations(comm):
	"""
	realiza comunicações via socket com o servidor dado um commando
	"""

	if comm == 'SYNC':
		# sincroniza server com client
		# 	gera dicionario de diferença
		# 	retorna payload e payload_size
		# 	envia payload
		# 	espera payload de resposta com a tree sincronizada
		# 	atualiza a tree atual e a ulta tree sincronizada
		pass

	if comm == "RESET_SERVER":
		# resetar servidor
		# 	deleta tudo do servidor
		#	last_sync_tree do servidor passa passa as ser uma tree vazia
		pass

	if comm == "GET_SERVER_FILELIST":
		# requisita a lista de arquivos atualmente no server. pode ser diferente da
		# last_synced_tree caso exitam mais de um usuário utilizando o programa.
		# 	envia payload com "OP": "GET_SERVER_FILELIST"
		# 	espera resposta com lista de arquivos
		# 	retorna resposta
		pass
	pass


# TODO : modularizar para se comunicar com a interface
def socket_conn_client():
	"""
	cria e admnistra socket que se conectará ao servidor.
	"""
	
	global SERVER_IP
	global PORT

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((SERVER_IP, PORT))

	while True:

		# TODO : modificar para receber estímulo da interface.

		# get user operation
		comm = input("> comm: ")
		
		# quit both on server and client
		if comm == 'quit':
			sock.send(comm.encode())
			break

		# treat server response.
		server_response = user_operation(comm)
		# treat_server_response(server_response)

	sock.close()


# TEST
if __name__ == "__main__":
	
	# global LAST_SYNC_TREE = json.loads(open("sync_tree.json", 'r').read())
	# global CURENT_TREE = LAST_SYNC_TREE

	socket_conn_client()
	print('Exiting...')