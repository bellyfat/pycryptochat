import socket




def run(host, port):
	server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	server.bind((host, port))
	
	clients = {}
	
	while 1:
		data, addr = server.recvfrom(65536)
		
		if addr[0] not in cleints.keys():
			if data not in people.values():
				people[addr[0]] = data
			else:
				people[addr[0]] = data + "_"
			continue
			
		data = data.strip()
		if data != '':
			print(f"{addr}:{data}")
			for i in clients:
				server.sendto(clients[addr[0]]+": " + data, (i,port))
		serv.close()

if __name__ == "__main__":
	run('localhost', 5005)
"""





















class Server:
	def __init__(self, host="", port="", timeout=-1):
		self.host = host
		self.port = port
		self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		self.sock.bind((host, port))
		self.recv_buffer = 4096
	
	
	# REVIEW
	def recv(self):
		while 1:
        ready_to_read,ready_to_write,in_error = select.select(SOCKET_LIST,[],[],0)

        for sock in ready_to_read:
            if sock == server_socket:
                sockfd, addr = server_socket.accept()
                SOCKET_LIST.append(sockfd)
                print "Client (%s, %s) connected" % addr
                broadcast(server_socket, sockfd, "[%s:%s] entered our chatting room\n" % addr)


            else:
                try:
                    data = sock.recv(RECV_BUFFER)
                    if data:
                        broadcast(server_socket, sock, "\r" + '[' + str(sock.getpeername()) + '] ' + data)
                    else:
                               if sock in SOCKET_LIST:
                            SOCKET_LIST.remove(sock)
                        broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                except:
                    broadcast(server_socket, sock, "Client (%s, %s) is offline\n" % addr)
                    continue
	
	def broadcast(server, sock, msg):
		
	
	

class Client:
"""