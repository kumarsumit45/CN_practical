import socket
from datetime import datetime

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 9999

server_socket.bind((host, port))

server_socket.listen(5)

print("Server waiting for incoming connections...")
while True:
    
    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    now = datetime.now()
    current_day_date_time = now.strftime("%A, %B %d, %Y %H:%M:%S")
    
    client_socket.send(current_day_date_time.encode('utf-8'))
    
    client_socket.close()
