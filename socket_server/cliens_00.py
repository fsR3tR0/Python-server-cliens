import socket 

c_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 12345
host = socket.gethostname()

c_socket.connect((host,port))
message = c_socket.recv(1024)
print(str(message.decode()))
c_socket.close()

