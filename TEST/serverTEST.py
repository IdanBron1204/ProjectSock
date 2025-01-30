import socket

#host = socket.gethostbyname(socket.gethostname())
# #another way(does not work with virtualbox)
HOST = '10.100.102.160'
PORT = 9090

listening_sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
listening_sock.bind((HOST,PORT))

listening_sock.listen(5)

while True:
    communication_sock, address = listening_sock.accept()#when a connection is accepted a tuple is received
    print(f"connected to {address}")
    message = communication_sock.recv(1024).decode('utf-8')#number of bytes that we want to receive(1024) and decode
    print(f'the message from the client is: {message}')
    communication_sock.send("the message is received TY".encode('utf-8'))
    communication_sock.close()
    print(f"connection with {address} ended")

