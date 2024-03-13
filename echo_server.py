import socket

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
    
    # Receive sentence from the client
    sentence = client_socket.recv(1024).decode()
    
    # Echo each word back to the client
    words = sentence.split()
    for word in words:
        client_socket.send(word.encode())
        client_socket.send(' '.encode())  # Add space between words
    
    # Close the connection with the client
    client_socket.close()