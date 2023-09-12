import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

my_address = ("localhost", 9900)
my_socket.bind(my_address)

is_running = True
while is_running:
    data, addr = my_socket.recvfrom(1024) # Сколько байт он принимает максимум(receive from)
    message = data.decode(encoding="UTF-8")
    print(f'Получено сообщение от {addr}: {data.decode(encoding="UTF-8")}')
    if message == "exit":
        is_running = False

# python server.py - как открывать файл, потом в ДРУГОМ ТЕРМИНАЛЕ написать python client.py
# Получено сообщение от ('127.0.0.1', 49961): Hello by UDP!
