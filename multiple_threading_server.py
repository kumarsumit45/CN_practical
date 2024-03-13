import socket
import threading

def handle_client(client_socket):
    while True:
        # Receive data from the client
        data = client_socket.recv(1024)
        if not data:
            break  # Exit the loop if no data is received

        # Process the received data (in this example, just echo it back)
        response = data.decode('utf-8')
        print(f"Received from {threading.current_thread().name}: {response}")

        # Send the response back to the client
        client_socket.sendall(data)

    # Close the client socket when the loop exits
    client_socket.close()

def multithreaded_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(5)

    print(f"Multithreaded server is listening on {host}:{port}...")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address}")

        # Create a new thread to handle the client
        client_handler = threading.Thread(target=handle_client, args=(client_socket,), daemon=True)
        client_handler.start()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    multithreaded_server(host, port)
