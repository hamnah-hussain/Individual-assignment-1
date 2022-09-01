# a TCP/IP client that receives a message from server
import socket
from bot import *
import random
import sys

#to start the client you need to write the ip, port and bot you want to use
ip = sys.argv[1]
port = int(sys.argv[2])
bot = sys.argv[3]

# create a socket at server side using TCP/IP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect it to server and port number
s.connect((socket.gethostname(), port))

#Associate the strings with the bots
bots = {"Al": Al, "Carter": Carter, "Bob": Bob, "Carlos": Carlos}

#Splits the sentence and find the type of action being used
def word(a):
    a = a.split()
    for word in a:
        if word in good_verbs: return word
        if word in bad_verbs: return word
        if word in greeting: return word
    return ""

#
while True:
    msg = s.recv(1024)
    print('Received: ' + msg.decode())
    if msg.decode().find("User") != -1:
        action = word(msg.decode())

    #check if its there
    if bot == "Al":
        response = Al(action)
    elif bot == "Carter":
        response = Carter(action)
    elif bot == "Bob":
        response = Bob(action)
    elif bot == "Carlos":
        response = Carlos(action)
    else:
        print("Choose one of these names: Ally, Carter, Bob, Carlos")

    #print(response)
    s.send(response.encode())
else:
    print("Another client")