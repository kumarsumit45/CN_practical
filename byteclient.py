import socket
import struct

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    # Receive the integer from the server
    received_data = client_socket.recv(4)  # Assuming the server sends a 4-byte integer
    unpacked_data = struct.unpack('!I', received_data)  # !I represents network byte order for an unsigned int

    print(f"Received data from server: {unpacked_data[0]}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
