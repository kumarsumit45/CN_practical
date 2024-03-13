import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = socket.gethostname()
port = 9999


client_socket.connect((host, port))

received_data = client_socket.recv(1024)

print(f"Received from server: {received_data.decode('utf-8')}")

client_socket.close()
