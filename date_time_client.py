import socket

# Server configuration
server_ip = '127.0.0.1'
server_port = 12345

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Receive date and time from the server
received_data = client_socket.recv(1024).decode()

# Print date and time in different rows
print("Date:", received_data.split()[0])
print("Time:", received_data.split()[1])

# Close the connection with the server
client_socket.close()
