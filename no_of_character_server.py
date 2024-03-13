#Counting no of characters

import socket

def count_characters(sentence):
    return len(sentence)

def start_server():
    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to a specific address and port
    host = '127.0.0.1'
    port = 12345
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(5)

    print(f"Server listening on {host}:{port}")

    while True:
        # Wait for a connection
        client_socket, addr = server_socket.accept()
        print(f"Connection from {addr}")

        # Receive data from the client
        data = client_socket.recv(1024).decode('utf-8')

        if not data:
            break

        # Process the data and send the result back to the client
        result = count_characters(data)
        client_socket.send(str(result).encode('utf-8'))

        # Close the connection
        client_socket.close()

if __name__ == "__main__":
    start_server()