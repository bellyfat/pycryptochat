import socket
import random
import sys
from time import sleep

def encrypt(text, key):
    global encrypted
    encrypted = int.from_bytes(text.encode('utf-8'), byteorder='big')
    encrypted = encrypted + key
    return encrypted

def decrypt(encrypted, key):
    encrypted = encrypted - key
    s = encrypted.to_bytes(encrypted, length=len(strg), byteorder='big').decode('utf-8')
    return text

def crypt(s,host,port):
    y = 121
    p = 22344323423
    message = 'h172hdx120o'
    s.sendto(message.encode(),(host,port))
    alpha = int(s.recv(1024).decode('UTF-8'))

    secret = random.randint(500,1000)
    beta = str(int((pow(y,secret) % p)))

    s.sendto(beta.encode(),(host,port))

    key = pow(alpha,secret) % p
    print("KEY: " +str(key))
    return key


def Main():
    host = 'localhost'
    port = int(sys.argv[1])
    key = 1

    s = socket.socket()
    s.connect((host, port))
    print("ASS!")

    message = input("-> ")
    while message != 'q':
        if message == 'c':
            key = crypt(s,host,port)
            message = 'Done!'
        message = str(encrypt(message, key))
        s.sendto(message.encode(),(host,port))
        data = s.recv(1024)
        data = decrypt(int(data),key)

        print("Alice: " + str(data.decode('UTF-8')))
        message = input("-> ")
    s.close()

if __name__ == '__main__':
    Main()
