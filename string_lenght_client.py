import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('127.0.0.1', 12345))

    # Send a message to the server
    message_to_send = "Hello, server!"
    client_socket.sendall(message_to_send.encode('utf-8'))

    # Receive the number of letters from the server
    received_data = client_socket.recv(1024).decode('utf-8')
    print(f"Number of letters received from server: {received_data}")

    client_socket.close()

if __name__ == "__main__":
    start_client()
