#Cameron Cottam
#UDP Calculator Client
import socket
import math

SERVER_NAME = 'localhost'
SERVER_PORT = 12345
#Takes the users input on what kind of sum they want to perfrom with what numbers.
CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
SUM = input('What calculation would you like to perform? (Use symbols)')
CLIENT_SOCKET.sendto(SUM.encode(),  (SERVER_NAME, SERVER_PORT))
NUM_1 = input('Please input the first number you want to use')
CLIENT_SOCKET.sendto(NUM_1.encode(),  (SERVER_NAME, SERVER_PORT))
NUM_2 = input('Please input the second number to want to use')
CLIENT_SOCKET.sendto(NUM_2.encode(), (SERVER_NAME, SERVER_PORT))

#Prints the answer that is retrived from the UDP server
ANSWER = CLIENT_SOCKET.recv(2048)
print("Answer: ", ANSWER.decode())

#The option for the user to continue using the same answer in the same or different sum.
Continue = input('Would you like to do a sum on to the current answer?')
while('y' in Continue):
    SUM = input('What calculation would you like to perform? (Use symbols)')
    CLIENT_SOCKET.sendto(SUM.encode(),  (SERVER_NAME, SERVER_PORT))
    NUM_1 = ANSWER.decode()
    print("Number 1:", NUM_1)
    CLIENT_SOCKET.sendto(NUM_1.encode(),  (SERVER_NAME, SERVER_PORT))
    NUM_2 = input('Please input the second number to want to use')
    print("Number 2:", NUM_2)
    CLIENT_SOCKET.sendto(NUM_2.encode(), (SERVER_NAME, SERVER_PORT))
    ANSWER = CLIENT_SOCKET.recv(2048)
    print("Answer: ", ANSWER.decode())
    Continue = input('Would you like to do a sum on to the current answer?')

CLIENT_SOCKET.close()
print("Connection close")
