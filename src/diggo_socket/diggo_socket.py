# Takes care of the socket operations

import socket
import json

class Diggo_socket_manager:

	def __init__ (self, sock, side, maxbuff=1024):
		self.SOCK = sock
		self.MAXBUFF = maxbuff
		self.SIDE = side

	def ready_payload(self, json_dict):
		"""
		dado dicionário, o transforma em numa string formatada
		para .json e retorna tanto o tamanho essa string ("payload")
		e o seu tamanho ("payload_size") em uma string de bytes.
		"""
		payload = json.dumps(json_dict).encode()
		payload_size = str(len(payload)).encode()

		return payload, payload_size


	# TODO : testar
	def send_payload(self, payload, payload_size):
		"""
		realiza a comunicação cliente/servidor,
		enviando primeiro o tamanho do payload principal
		para preparar o servidor para recebêlo, e depois
		o seu conteúdo.
		"""

		# send() buffsize
		print(self.SIDE + " send() buff.")
		self.SOCK.send(payload_size)

		# recv() feedback
		print(self.SIDE + " recv() feedback.")
		response = self.SOCK.recv(1024).decode()
		if response != "True":
			print("[ERROR!"+ self.SIDE +"]: " + response)
			return False

		# send() payload
		print(self.SIDE + " send() payload.")
		self.SOCK.send(payload)

		print("")
		return True

	# TODO : testar
	def recv_payload(self):
		"""
		função recv do socket adaptada para a aplicação. retorna
		um json em forma de string.
		"""

		# recv() payload_size
		payload_size = int(self.SOCK.recv(self.MAXBUFF).decode())
		print(self.SIDE + " recv() payload_size.")

		# send() got payload_size
		print(self.SIDE + " send() payload_size OK.")
		self.SOCK.send(b'True')

		# recv() message loop
		print(self.SIDE + " recv() payload loop.")
		data = ''
		chunks = -(-payload_size//self.MAXBUFF) # teto da divisão entre payload_size e MAXBUFF
		for i in range(chunks):
			p_data = self.SOCK.recv(self.MAXBUFF)
			print('p_data: ' + p_data.decode())
			data += p_data.decode()

		# visualize data
		print("[" + self.SIDE+ " GOT]: "+ data)

		# return string
		return data