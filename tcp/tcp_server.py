#! /usr/bin/python3

import socket

s_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
port = 12345
host = socket.gethostname()
#print(port,host)
s_server.bind((host,port))
message = "Halo Cliens"

s_server.listen(5)

def main():
	while True:
		print("Waiting for connection...")
		client_socket,addr = s_server.accept()
		print("[+] Client connected from " + str(addr))
		while True:
			data = client_socket.recv(1024)
			if not data or data.decode == 'END':
				break
			print("[+] Received data: %s", %data.decode('utf-8'))
			try:
				client_socket.send(message.encode('utf-8'))
			except:
				print("[+] Client disconnected - %s",%str(addr))
		client_socket.close()
	server_socket.close()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\n")
		print("[+] Server shutdown ...")

