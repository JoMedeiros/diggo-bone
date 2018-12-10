#!/usr/bin/env python3

import socket
import json
import time

# user defined modules
#import calc_diff
import diggo_socket as ds

MAXBUFF = 1024
SERVER_IP = "127.0.0.1"
PORT = 9999

SKCT_MAN = ''

# TODO : implementar e testar 'SYNC' [PRIORIDADE].
def treat_user_comm(comm):
	"""
	realiza comunicações via socket com o servidor dado um commando
	"""

	global SKCT_MAN

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

	if comm == "TEST":
		# testar modulos
		# simple json
		p , p_size = SKCT_MAN.ready_payload({ "OP": "TEST", "BODY": "I am client testing."})
		SKCT_MAN.send_payload(p, p_size)
		return 'TEST'

	if comm == 'QUIT':
		# encerrar programa no servidor e no client
		# TODO: fechar apaneas no client. timeout no servidor
		print("\t reading payload...")
		p , p_size = SKCT_MAN.ready_payload({ "OP": "QUIT", "BODY": "I am client testing."})
		print("\t sending payload...")
		SKCT_MAN.send_payload(p, p_size)
		print("\t reciving payload...")
		data = json.loads(SKCT_MAN.recv_payload())
		print("\t print what i got as \'data\'...")
		print(data)
		print("\t return data...")
		return data['OP']

	pass

# TODO : modularizar para se comunicar com a interface
def create_client_socket():
	"""
	cria e admnistra socket que se conectará ao servidor.
	"""
	
	global SERVER_IP
	global PORT
	global SKCT_MAN

	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((SERVER_IP, PORT))

	SKCT_MAN = ds.Diggo_socket_manager(sock, 'CLIENT')

	while True:

		# TODO : modificar para receber estímulo da interface.

		# treat server response.
		server_response = treat_user_comm(input("> comm: "))
		# TEST : 
		print(str(server_response))
		if server_response == 'QUIT':
			break
		# treat_server_response(server_response)

	print('closing socket...')
	sock.close()


# TEST
if __name__ == "__main__":
	
	# global LAST_SYNC_TREE = json.loads(open("sync_tree.json", 'r').read())
	# global CURENT_TREE = LAST_SYNC_TREE

	create_client_socket()
	print('Exiting...')