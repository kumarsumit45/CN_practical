import socket
from datetime import datetime

# Server configuration
server_ip = '127.0.0.1'
server_port = 12345

# Create socket object
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((server_ip, server_port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {server_ip}:{server_port}")

while True:
    # Accept a connection from a client
    client_socket, client_address = server_socket.accept()
    
    # Get current date and time
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Send date and time to the client
    client_socket.send(current_datetime.encode())
    
    # Close the connection with the client
    client_socket.close()
