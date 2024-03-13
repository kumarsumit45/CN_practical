import socket

# Configure the client
host = '127.0.0.1'
port = 55555

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))

# Send a request for date to the server
client_socket.send("date".encode('utf-8'))

# Receive and print the response
date_response = client_socket.recv(1024).decode('utf-8')
print("Server Date:", date_response)

# Close the connection
client_socket.close()
