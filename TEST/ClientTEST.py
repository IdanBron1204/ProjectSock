import socket

HOST = '10.100.102.160'
PORT = 9090
#when connecting with server not in you LAN you need to put the public ip address from myip.is
sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sock.connect((HOST,PORT))#server ip,server port

sock.send("hi server".encode('utf-8'))
message = sock.recv(1024).decode()
print ('the server said:'
       f'{message}')


