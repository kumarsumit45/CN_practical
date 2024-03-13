import socket
import struct

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 12345))
    server_socket.listen(1)

    print("Server listening on port 12345")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connection from {client_address}")

        # Send an integer (42) to the client
        data_to_send = 42
        packed_data = struct.pack('!I', data_to_send)  # !I represents network byte order for an unsigned int
        client_socket.sendall(packed_data)

        client_socket.close()

if __name__ == "__main__":
    start_server()
