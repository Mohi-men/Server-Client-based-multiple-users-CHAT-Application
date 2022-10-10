import socket
import threading
import re

stop = False
flag = False
# s_ = False


def connect():
    # Choosing Nickname
    global nickname, client
    nickname = input("Choose your nickname: ")

    # Connecting To Server
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect(('127.0.0.1', 1234))

def allow():
    global write_thread
    write_thread.start()

    
# Listening to Server and Sending Nickname
def receive(s):
    while True:
        try:
            # Receive Message From Server
            message = client.recv(1024).decode('ascii')
            if message == 'NICK':
                client.send(nickname.encode('ascii'))
            else:
                if message[0] == '0':
                    print(message[1:])
                    client.close()
                    global stop 
                    stop = True
                    if stop: break

                elif message[0] == '>':
                    print(message.split(":",1)[0]+ ": " +decrypt(message.split(":",1)[-1]))
                else:
                    global flag
                    if not flag:
                        allow()                        
                        flag = True
                    print(message)
        except:
            # Close Connection When Error
            print("An error occured!")
            client.close()
            break


# Sending Messages To Server
def write(s):
    while True:
        message = '{}'.format(input(''))
        matched = re.match("^[a-z/0-9/A-Z]+[*]+", message)
        if not bool(matched):
            print("Invalid protocol!! try with this format: [ALL/nickname]*message")
        else:
            temp = message.split("*",1)[0]
            temp += "*"
            temp += encrypt(str(message.split("*",1)[-1]))
            client.send(temp.encode('ascii'))


#encryption function
def encrypt(text):
    new = ""
    for i in text:
        value = ord(i)
        if value >= 65 and value <= 90:
            if value + 1 > 90:
                value = 65
            else:
                value += 1
        elif value >= 97 and value <= 122:
            if value + 1 > 122:
                value = 97
            else:
                value += 1
        
        new += chr(value)
    return new

#decryption function
def decrypt(text):
    new = ""
    for i in text:
        value = ord(i)
        if value >= 65 and value <= 90:
            if value - 1 < 65:
                value = 90
            else:
                value -= 1
        elif value >= 97 and value <= 122:
            if value - 1 < 97:
                value = 122
            else:
                value -= 1
        
        new += chr(value)
    return new



connect()
# Starting Threads For Listening And Writing
receive_thread = threading.Thread(target=receive, args =(stop, ))
receive_thread.start()
write_thread = threading.Thread(target=write, args =(stop, ))



    
    