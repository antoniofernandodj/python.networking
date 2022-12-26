from socket import socket


###############


# Server:
 
s = socket()        
port = 12345
sckt = ('', port)
s.bind(sckt)
s.listen(5)

loop = True
while loop:
    connection, address = s.accept()
    print('Got connection from', address)
    connection.send('Thank you for connecting'.encode())
    connection.close()
    data = b''
    data_to_receive = True
    while data_to_receive:
        d = connection.recv(1024)
        data += d
        if len(d) < 1:
            data_to_receive = False
        if not data_to_receive:
            connection.sendall(data)
