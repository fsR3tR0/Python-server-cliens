#! /usr/bin/python3

import socket

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
host = socket.gethostname()
#print(port,host)
c_socket.connect((host,port))
global message
message  = "Halo Server!"

def main():
	global message
	while True:
		c_socket.send(message.encode('utf-8'))
		data = c_socket.recv(1024)
		print(str(data.decode('utf-8')))
		more = input("Want Sir/Lady send more data?(y/n)\n")
		if more.lower() == 'y':
			message = input("Write please the message:\n")
		else:
			break
	c_socket.close()

if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\n")
		print("[+] Client shutdown") 

