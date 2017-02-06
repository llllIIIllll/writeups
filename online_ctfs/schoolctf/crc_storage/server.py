import SocketServer
from crc import crc32

val = 0x123123

f = open("flag.txt")
FLAG = f.read()
f.close()

class MyTCPHandler(SocketServer.BaseRequestHandler):
		def handle(self):
			self.request.sendall("Hello, this is flag storage service.\nif you give me right pass, then i give you flag.\nYou pass: ")
			data = self.request.recv(100500)
			if crc32(data) == val:
				self.request.send(FLAG + "\n")
			else:
				self.request.send("Sorry\n")


if __name__ == "__main__":
	HOST, PORT = "0.0.0.0", 12345
	SocketServer.TCPServer.allow_reuse_address = True
	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
	server.serve_forever()

