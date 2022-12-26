from socket import (
    gethostbyname,
    AF_INET,
    SOCK_STREAM,
    socket
)

host_ip = gethostbyname('www.google.com')
sckt = (host_ip, 80)
mysock = socket(AF_INET, SOCK_STREAM)
mysock.connect(sckt)

