import socket
# SOCK_STREAM - TCP


my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# server_adress = ('192.168.110.190', 7777)
# server_adress = ('192.168.111.69', 7777) семен
server_adress = ('192.168.110.190', 7777)


message = 'привет!'
data  = message.encode('utf8')
my_socket.sendto(data, server_adress)