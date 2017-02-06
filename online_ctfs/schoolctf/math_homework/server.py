import SocketServer
from Crypto.Cipher import AES
from key import key, FLAG
from Crypto.Util import Counter

menu = """Hello, this is math homework crypto server. Choose:
	
First: solve linear
Second: solve quadratic
Third: solve cubic
"""

linear = lambda x: 5 * x + 5
quadratic = lambda x: x ** 2 + 5 * x + 4
cubic = lambda x: x ** 3 + 2 * x ** 2 + x + 2



class MyTCPHandler(SocketServer.BaseRequestHandler):
		def handle(self):
			ctr = Counter.new(16 * 8)
			cryptor = AES.new(key, AES.MODE_CTR, counter=ctr)
			self.request.sendall(cryptor.encrypt(menu))
			while True:
				choice = cryptor.decrypt(self.request.recv(100500)).split('\n')[0]
				if choice == "First":
					self.request.send(cryptor.encrypt("send me answer on this equation: 5 * x + 5"))
					x = int(cryptor.decrypt(self.request.recv(160033)).split(' ')[0])
					if linear(x) == 0:
						self.request.send(cryptor.encrypt("Good"))
					else:
						self.request.send(cryptor.encrypt("Bad"))
				elif choice == "Second":
					self.request.send(cryptor.encrypt("send me answer on this equation: x ** 2 + 5 * x + 4"))
					x = int(cryptor.decrypt(self.request.recv(160033)).split(' ')[0])
					if quadratic(x) == 0:
						self.request.send(cryptor.encrypt("Good"))
					else:
						self.request.send(cryptor.encrypt("Bad"))
				elif choice == "Third":
					self.request.send(cryptor.encrypt("send me answer on this equation: x ** 3 + 2 * x ** 2 + x + 2"))
					x = int(cryptor.decrypt(self.request.recv(105000)).split(' ')[0])
					if cubic(x) == 0:
						self.request.send(cryptor.encrypt(FLAG))	
					else:
						self.request.send(cryptor.encrypt("Bad"))
				else:
					self.request.send(cryptor.encrypt("Sorry"))
					return


if __name__ == "__main__":
	HOST, PORT = "0.0.0.0", 54321
	SocketServer.TCPServer.allow_reuse_address = True
	server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)
	server.serve_forever()
