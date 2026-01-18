import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect = ('localhost', 12345)
client.connect(connect)
print(f'Клиент подключился к серверу по адресу {connect}')

message = 'Как дела!'
client.send(message.encode())

response = client.recv(1024)
print(response.decode())

client.close()