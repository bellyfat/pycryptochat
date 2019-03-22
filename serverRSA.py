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

def crypt(host,port,c):
    y = 121
    p = 22344323423
    secret = random.randint(1,499)
    alpha = str(int((pow(y,secret) % p)))

    c.sendto(alpha.encode(),(host,port))

    beta = int(c.recv(1024).decode('UTF-8'))

    key = pow(beta,secret) % p
    print("KEY: " +str(key))
    return key


def Main():
    host = 'localhost'
    port = int(sys.argv[1])
    key = 1

    s = socket.socket()
    s.bind((host, port))

    s.listen(3)
    c, addr = s.accept()
    print("Connection from: " + str(addr))

    while True:

        data = c.recv(1024).decode('UTF-8')
        data = decrypt(int(data),key)

        if data == 'h172hdx120o':
            key = crypt(host,port,c)
        else:
            print("Bob: " + str(data))
            data = input("-> ")
            data = encrypt(data,key)
            c.sendto(data.encode(),(host,port))
    c.close

if __name__ == '__main__':
    Main()
