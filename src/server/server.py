#!/usr/bin/env python3

import socket
import json
import time

MAXBUFF = 1024
MAXUSERS = 1
HOST = ''
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
def socket_recv_payload(sock, first_data):
	"""
	função recv do socket adaptada para a aplicação. retorna
	um json em forma de string.
	"""

	global MAXBUFF

	# get payload_size for main payload
	payload_size = int(first_data.decode())
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
	print('[SERVER GOT]: ' + data)

	return data

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
		request = socket_recv_payload(conn, data)
		# treat_client_request(client_response)

		print("")

	print('closing socket...')
	conn.close()			
	sock.close()

if __name__ == "__main__":
	create_server_socket()
	print('Exiting...')