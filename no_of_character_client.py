#Counting no of characters

import socket

def send_sentence_to_server(sentence):
    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    host = '127.0.0.1'
    port = 12345
    client_socket.connect((host, port))

    # Send the sentence to the server
    client_socket.send(sentence.encode('utf-8'))

    # Receive the result from the server
    result = client_socket.recv(1024).decode('utf-8')

    print(f"Number of characters in the sentence: {result}")

    # Close the connection
    client_socket.close()

if __name__ == "__main__":
    user_input = input("Enter a sentence: ")
    send_sentence_to_server(user_input)