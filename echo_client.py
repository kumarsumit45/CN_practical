import socket

# Server configuration
server_ip = '127.0.0.1'
server_port = 12345

# Create socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((server_ip, server_port))

# Input sentence from the user
sentence = input("Enter a sentence: ")

# Send the sentence to the server
client_socket.send(sentence.encode())

# Receive and print the echoed sentence
echoed_sentence = client_socket.recv(1024).decode()
print(f"Echoed Sentence: {echoed_sentence}")

# Close the connection with the server
client_socket.close()