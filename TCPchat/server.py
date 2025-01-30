import socket
import threading

HOST = 'localhost'  # 127.0.0.1
PORT = 8080

listening_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listening_sock.bind((HOST, PORT))
listening_sock.listen()

clients = []
nicknames = []

# Sending Messages To All Connected Clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handling Messages From Clients
def chat_manager(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            broadcast(message)
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left'.encode())
            nicknames.remove(nickname)
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        communication_sock, address = listening_sock.accept()
        print(f"Connected with {address}")

        # Request And Store Nickname
        communication_sock.send('NICKNAME'.encode())
        nickname = communication_sock.recv(1024).decode()
        nicknames.append(nickname)
        clients.append(communication_sock)

        # Print And Broadcast Nickname
        print(f'His nickname is {nickname}')
        broadcast(f"{nickname} has joined!".encode())
        communication_sock.send('Connected successfully'.encode())

        # Start Handling Thread For Client
        thread = threading.Thread(target=chat_manager, args=(client,))
        thread.start()

print("Server is listening....")
receive()