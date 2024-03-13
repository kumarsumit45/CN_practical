import socket
import os

#handle client if forking succesful
def handle_client(conn,addr):
	while True:
		data=conn.recv(1024)
		if not data:
			print("Client Disconnected")
			break
		print("Data from client: ",data.decode())

#main
host=socket.gethostname()
port=12345

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host,port))
s.listen(5)
print("Socket now listening")
while True:
	conn,addr=s.accept()
	print('Connected to:',addr[0],':',addr[1])
	child_pid=os.fork() 
	if child_pid==0:
		print("Child process started")
		handle_client(conn,addr)
	else:
		print("Child process did not start")
	s.close()