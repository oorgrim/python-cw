import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_addr = ('192.168.111.21', 7777)

my_socket.bind(my_addr)

data, addr = my_socket.recvfrom(2048)
message = data.decode('utf8')

print(f"Сообщение: {message} от {addr}")

# IPC

running = True
while running:
    data, addr = my_socket.recvfrom(2048)
    message  = data.decode('utf8')
    print(f"Сообщение: {message} от {addr}")
    if message == 'exit':
        running = False