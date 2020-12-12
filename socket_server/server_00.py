import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host,port))
global data_send
data_send = "Halo"

s.listen(5)

def main():
	global data_send
	while True:
		c,addr = s.accept()
		print("[+] Connection: " + str(addr))
		c.send(data_send.encode())
		c.close()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\n[+] Shutdown")
		s.close()

