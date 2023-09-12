import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_address = ('localhost', 9900)

# message = 'Hello by UDP!'

while is_running:
    message = input('Введите что-нибудь(желательно на английском): ')
    my_socket.sendto(message.encode(), server_address)
    if message = 'exit':
        my_socket.sendto(message.encode(), server_address)






# python client.py - как открывать файл
# Выходит сообщение сверху если открыть СРАЗУ 2 ТЕРМИНАЛА

# Получено сообщение от ('127.0.0.1', 55829): Hello by UDP!

# Получено сообщение от ('127.0.0.1', 60015): exit
