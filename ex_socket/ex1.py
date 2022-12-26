from socket import AF_INET, SOCK_STREAM, socket

sckt = ('data.pr4e.org', 80)
loop = True
data = b''
connected = False
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
with socket(AF_INET, SOCK_STREAM) as sender:
    while not connected:
        try:
            sender.connect(sckt)
            connected = True

        except ConnectionRefusedError:
            print('Server not connected')
            import time
            time.sleep(3)

    sender.send(cmd)

    total_data = b''
    data_to_be_received = True
    while data_to_be_received:
        d = sender.recv(2)
        total_data += d
        if len(d) < 1:
            data_to_be_received = False
            total_data = total_data.decode()

# 1: Criar o elemento socket

# 2: Conectar a uma tupla host, porta

# 3: Abrir um loop inf de tentativa de conexão

# 4: Tentar conectar, se nao conseguir levantar excessao. se consegui, fechar loop inf

# 5: enviar mensagem

# 6: Abrir loop para saber quando manter conexão

# 7: Receber dados em stream, e ir passando aos poucos para um acumulador

# 8: se os dados forem de tamanho menor menores que 1, encerrar loop

# 9: decodificar dados recebidos para utf8
