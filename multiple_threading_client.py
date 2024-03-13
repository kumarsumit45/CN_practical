import socket

def client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    while True:
        message = input("Enter a message (or 'exit' to quit): ")
        if message.lower() == 'exit':
            break

        client_socket.sendall(message.encode('utf-8'))
        response = client_socket.recv(1024)
        print("Server response:", response.decode('utf-8'))

    client_socket.close()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 12345
    client(host, port)

