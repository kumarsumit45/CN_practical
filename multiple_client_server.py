import socket
import threading
import datetime

def handle_client(client_socket, client_address):
    print(f"Accepted connection from {client_address}")

    try:
        request = client_socket.recv(1024).decode('utf-8')

        if request == "date":
            response = datetime.datetime.now().strftime("%Y-%m-%d")
        elif request == "time":
            response = datetime.datetime.now().strftime("%H:%M:%S")
        else:
            response = "Invalid request"

        client_socket.send(response.encode('utf-8'))

    except Exception as e:
        print(f"Error handling client {client_address}: {str(e)}")

    print(f"Connection from {client_address} closed.")
    client_socket.close()

# Configure the server
host = '127.0.0.1'
port = 55555

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to a specific address and port
server_socket.bind((host, port))

# Listen for incoming connections
server_socket.listen()

print(f"Server listening on {host}:{port}")

# Accept and handle incoming connections
while True:
    client_socket, client_address = server_socket.accept()

    # Start a new thread to handle the client
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
