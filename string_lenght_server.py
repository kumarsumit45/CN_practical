import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Server listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Receive the message from the client
        received_data = client_socket.recv(1024).decode('utf-8')
        print(f"Received message from client: {received_data}")

        # Calculate the number of letters in the message
        num_letters = sum(c.isalpha() for c in received_data)

        # Send the number of letters back to the client
        client_socket.sendall(str(num_letters).encode('utf-8'))

        client_socket.close()

if __name__ == "__main__":
    start_server()
