import queue
import threading
import socket

messages = queue.Queue()
clients = []

communication_sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
communication_sock.bind(('localhost',8080))



def receive():
    while True:
        try:
            message,address = communication_sock.recvfrom(1024)
            messages.put((message,address))
        except:
            pass

def brodcast():
    while True:
        while not messages.empty():
            message , address = messages.get()
            print(message.decode())
            if address not in clients:
                clients.append(address)
            for client in clients:
                try:
                    if message.decode().startswith("SIGNUP_TAG"):
                        name = message.decode()[message.decode().index(":") + 1:]
                        communication_sock.sendto(f"{name} joined".encode(), client)
                    else:
                        communication_sock.sendto(message,client)
                except:
                    clients.remove(client)

t1 = threading.Thread(target=receive)
t2 = threading.Thread(target=brodcast)
print('Server is On')
t1.start()
t2.start()
