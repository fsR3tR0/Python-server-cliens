#! /usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler

class echoHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		self.wfile.write("Fut a HTTP genyo".encode())
		#self.wfile.write(self.path[1:0].encode())


def main():
	Port = 8000
	server = HTTPServer(('',Port),echoHandler)
	print("Server running on port %s" % Port)
	server.serve_forever()



if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt:
		print("\n[+] HTTPServer shutdown")

