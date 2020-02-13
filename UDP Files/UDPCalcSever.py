#Cameron Cottam
#UDP Calculator Server-Side

import socket
import math
SERVER_PORT = 12345
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ANSWER = 0
SERVER_SOCKET.bind(('localhost', SERVER_PORT))
print('The server is ready')
while 1: #While the loop is playing, the server prints out the values that the user has sent.
         #This is then matched with the if statements to perform the right calculation.
    SUM, CLIENT_ADDRESS = SERVER_SOCKET.recvfrom(2048)
    print('SUM:,', SUM)
    NUM_1, CLIENT_ADDRESS = SERVER_SOCKET.recvfrom(2048)
    print('Number 1: ', NUM_1)
    NUM_2, CLIENT_ADDRESS = SERVER_SOCKET.recvfrom(2048)
    print('Number 2: ', NUM_2)
    if '+' in SUM.decode():
        ANSWER = float(NUM_1.decode()) + float(NUM_2.decode())
    elif '-' in SUM.decode():
        ANSWER = float(NUM_1.decode()) - float(NUM_2.decode())
    elif '/' in SUM.decode():
        ANSWER = float(NUM_1.decode()) / float(NUM_2.decode())
    elif '*' in SUM.decode():
        ANSWER = float(NUM_1.decode()) * float(NUM_2.decode())

    print("Answer: ", ANSWER)
    SERVER_SOCKET.sendto(str(ANSWER).encode(), CLIENT_ADDRESS)
    
print("Client has disconnected")
SERVER_SOCKET.close()

