# a TCP/IP server that sends a messages to client
import socket
import sys
import threading

# take the port number
port = int(sys.argv[1])

# create a socket at server side using TCP/IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket with server server and port numner
s.bind((socket.gethostname(), port))


# allow maximum 4 connection to the socket
s.listen(4)

#Create an array for all the clients
client_array = []
def accept_client():
    while True:
        c, addr = s.accept()
        client_array.append(c)
        print("\nA member has joined!")

threading.Thread(target=accept_client, daemon=True).start()

while True:
    suggestion = input("Write a suggestion: ")
    for client in client_array:
        client.send(("User: " + suggestion).encode())
    for client in client_array:
        msg = client.recv(1024)
        print(msg.decode())
        for c in client_array:
            if c != client: c.send(msg)