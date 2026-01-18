import socket

history_data = []
socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_adress = (('localhost', 12345))
socket.bind(server_adress)
socket.listen(10)

while True:
    client_socket, client_adress = socket.accept()
    print(f'Пользователь с адресом: {client_adress} подключился к серверу')

    data = client_socket.recv(1024).decode()
    print(f'Пользователь с адресом: {client_adress} отправил сообщение: {data}')
    history_data.append(data)

    response = f'{history_data}'
    client_socket.send('\n'.join(history_data).encode())

    client_socket.close()

if __name__ == '__main__':
    server()





