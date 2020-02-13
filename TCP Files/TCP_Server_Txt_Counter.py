#Cameron Cottam
#TCP word & letter counter
#Server-side

import socket

SERVER_HOST = '127.0.0.1'
SERVER_PORT = 54321
#Two varaliables for the Number of letters and words
NumChars = 0
NumWords = 0
SERVER_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER_SOCKET.bind((SERVER_HOST, SERVER_PORT))
print("Server starting up, waiting for connection")
SERVER_SOCKET.listen(1)

INCOMING_CONNECTION, CLIENT_ADDRESS = SERVER_SOCKET.accept()
print("Connection has been established")
INCOMING_FILE_Name = INCOMING_CONNECTION.recv(4096)
INCOMING_FILE_DATA = INCOMING_CONNECTION.recv(4096)
print(INCOMING_FILE_DATA.decode())
# This section reads the file and performs a for loop to count the number of words and letters
with open(INCOMING_FILE_Name.decode(), "r") as file:
    for line in file:
        Wordslist = line.split()
        NumWords += len(Wordslist)
        NumChars += len(line)


print(NumWords)
print(NumChars)
INCOMING_CONNECTION.sendall(str(NumWords).encode())
INCOMING_CONNECTION.sendall(str(NumChars).encode())
SERVER_SOCKET.close()
