#Cameron Cottam
#TCP word & letter counter
#Client-Side
import socket


SERVER_HOST = '127.0.0.1'
SERVER_PORT = 54321

CLIENT_SOCKET = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

CLIENT_SOCKET.connect((SERVER_HOST, SERVER_PORT))

#Asks the user to enter the name of the text file then reads the data and closes it.
FILENAME = input(str("What text file would you like to upload?"))
f = open(FILENAME, "r")
FILE_DATA = f.read(4096).encode()
f.close()

#Prints the data and sends it along with the file to the server
print(FILE_DATA)
CLIENT_SOCKET.sendall(str(FILENAME).encode())
CLIENT_SOCKET.sendall(str(FILE_DATA).encode())

print("Data is sent")
#Receives the number of words and letters. Then prints them out.
RECEIVED_WORDS, SERVER_HOST = CLIENT_SOCKET.recvfrom(4096)
RECEIVED_CHAR, SERVER_HOST = CLIENT_SOCKET.recvfrom(4096)
print("Data received from TCP server")

print("Number of words and characters in ", FILENAME)
print(RECEIVED_WORDS.decode())
print(RECEIVED_CHAR.decode())

CLIENT_SOCKET.close()
