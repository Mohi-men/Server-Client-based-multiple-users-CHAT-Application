import socket
import threading
import re

# Connection Data
host = '127.0.0.1'
port = 1234

# Starting Server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((host, port))

server.listen()


print("Server is Listening...")
# Lists For Clients and Their Nicknames
clients = []
nicknames = []



# Sending Messages To All Connected Clients
def broadcast(message,client):
	#print(nicknames)

	for inTheArrayclient in clients:
		if (inTheArrayclient != client):
			inTheArrayclient.send(message)



# Handling Messages From Clients
def handle(client):
    while True:
        try:
            # Broadcasting Messages
            message = client.recv(1024)
            nickname = message.decode('ascii').split("*",1)[0]
            text = message.decode('ascii').split("*",1)[-1]
            sender = nicknames[clients.index(client)]

            if nickname == 'ALL':
                temp = ">> (broadcast)"
                temp += sender + ": " + text
                broadcast(temp.encode('ascii'),client)
            elif nickname in nicknames:
                index = nicknames.index(nickname)
                receiver = clients[index]
                temp = ">> "
                temp += sender + ": " + text
                receiver.send(temp.encode('ascii'))
            else:
                client.send('Client not found!'.encode('ascii'))
        except:
            # Removing And Closing Clients
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]

            broadcast('{} left!'.format(nickname).encode('ascii'),client)
            nicknames.remove(nickname)
            break


# Receiving / Listening Function
def receive():
    while True:
        # Accept Connection
        client, address = server.accept()
        print("Connected with {}".format(str(address)))

        # Request And Store Nickname
        client.send('NICK'.encode('ascii'))
        
        nickname = client.recv(1024).decode('ascii')
        if nickname not in nicknames + ['ALL']:
            nicknames.append(nickname)
            clients.append(client)

            # Print And Broadcast Nickname
            print("Nickname is {}".format(nickname))
            
            broadcast("{}  just joined the server!\n".format(nickname).encode('ascii'),client)
            
            client.send('Connected to server!'.encode('ascii'))

            # Start Handling Thread For Client
            thread = threading.Thread(target=handle, args=(client,))
            thread.start()
        else:
            client.send('0Try different nickname!'.encode('ascii'))
            client.close()


receive()

