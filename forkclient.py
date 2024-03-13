import socket
host = socket.gethostname()
port= 12345

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host,port))

while True:
	send_data=input("Enter data to send: ")
	s.send(str(send_data).encode())
	
	ch=input("Want to continue[y/n]: ")
	if ch=='y':
		continue
	else:
		break
	s.close()