#!/usr/bin/env python3

import socket
import json
#import calc_diff

SERVER_IP = "127.0.0.1"
PORT = 9999

def ready_payload(json_dict):
	"""
	dado dicionário, o transforma em numa string formatada
	para .json e retorna tanto o tamanho essa string ("payload")
	e o seu tamanho ("payload_size") em uma string de bytes.
	"""
	payload = json.dumps(payload).encode()
	payload_size = str(len(payload)).encode()

	return payload, payload_size


# TODO : implementar e testar 'SYNC'.
def user_operations(comm):
	"""
	gera payload dado uma operação
	"""

	if comm == 'SYNC':
		# gera dicionario de diferença
		# retorna payload e payload_size
		# envia payload
		# espera payload de resposta com a tree sincronizada
		# atualiza a tree atual e a ulta tree sincronizada
		pass
	#if comm == "RESET_SERVER":
		# deleta tudo do servidor
	pass


# TODO : testar
def socket_talk(sock, payload, payload_size):
	"""
	realiza a comunicação cliente/servidor,
	enviando primeiro o tamanho do payload principal
	para preparar o servidor para recebêlo, e depois
	o seu conteúdo.
	"""

	# send() buffsize
	sock.send(payload_size)

	# recv() server feedback
	response = sock.recv(1024).decode()
	if response != "True":
		print("[ERROR!SERVER]: " + response)
		return False

	# send() payload
	sock.send(payload)

	# recv() server feedback
	response = sock.recv(1024).decode()
	if response != "True":
		print("[ERROR!SERVER]: " + response)
		return False

	print("")
	return True


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

		# get user operation
		comm = input("> comm: ")
		
		# quit both on server and client
		if comm == 'quit':
			sock.send(comm.encode())
			break

		# decide user operation
		payload, payload_size = user_operations(comm)
		# speak to server
		socket_talk(sock, payload, payload_size)

	sock.close()


# para tests
if __name__ == "__main__":
	
	# global LAST_SYNC_TREE = json.loads(open("sync_tree.json", 'r').read())
	# global CURENT_TREE = LAST_SYNC_TREE

	socket_conn_client()
	print('Exiting...')