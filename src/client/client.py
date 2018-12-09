#!/usr/bin/env python3

import socket
import json
#import calc_diff

MAXBUFF = 1024
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


# TODO : testar
def socket_send_payload(sock, payload, payload_size):
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
	#response = sock.recv(1024).decode()
	#if response != "True":
	#	print("[ERROR!SERVER]: " + response)
	#	return False


	print("")
	return True

# TODO : testar
def socket_recv_payload(sock, size_data):
	"""
	função recv do socket adaptada para a aplicação. retorna
	um json em forma de string.
	"""

	global MAXBUFF

	# get payload_size for main payload
	payload_size = int(size_data.decode())
	print("payload_size: " + str(payload_size))

	# send() got payload_size
	sock.send(b'True')

	# recv() message loop
	data = ''
	chunks = -(-payload_size//MAXBUFF) # teto da divisão entre payload_size e MAXBUFF
	for i in range(chunks):
		p_data = sock.recv(MAXBUFF)
		print('p_data: ' + p_data.decode())
		data += p_data.decode()
		#time.sleep(.5)

	# visualize data
	print('[CLIENT GOT]: ' + data)

	return data

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