from socket import socket

s = socket()

port = 12345

sckt = ('127.0.0.1', port)
s.connect(sckt)

msg = s.recv(1024).decode()
print(msg)

s.close()


