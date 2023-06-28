""" A multi-threaded tcp server """

import socket 
import threading 
import argparse 
import sys


# defining argument parsers 
parser = argparse.ArgumentParser()
parser.add_argument('-a','--address', type=str, help="Host IP Address (server address) ")
parser.add_argument('-p','--port', type=int, help="Host Port Number (server port number)")
arg = parser.parse_args()


# Ip and Port for our server  
address = arg.address
port = arg.port 

# check if address address is not none 
if not address:
	print("You didn't provide an ip address, the default address 127.0.0.1 will be used")
	address = "127.0.0.1" 

# check if port in none 
if not port:
	print("You didn't provide a port number, so the default port 9080 will be used")
	port = 9070


# fuction to listen and accept all connections  
def main():
	# seting socket type to ipv4 and tcp 
	server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

	# try to bind address and port 
	try:
		print(f"[+] Listening on {address}:{port}")
	except:
		print(f"Unable to establish connection on {address}:{port}")
		sys.exit()

	server.bind((address,port))
	# listen for connection and allow 5 connection request in pending state before they are accepted 
	server.listen(5)

	# accept an handle connection  
	while True:
		client, addr = server.accept()
		hostname = socket.gethostname()
		print(f"[+] connection accepted from {hostname} on {addr[0]}:{addr[1]}")

		# run handle_client function concurrently 
		client_handler = threading.Thread(target=handle_client, args=(client, ))
		client_handler.start()



# handle client , recieve and send data 
def handle_client(client_socket):
	while True:
		data, address= client_socket.recvfrom(1024)
		
		# get client hostname 
		name = socket.gethostname()
		print(f"[+][+]{name}: {data.decode('utf-8')} \n")
		


if __name__ == '__main__':
	main()

































