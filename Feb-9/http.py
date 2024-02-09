import socket

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_addr = ('192.168.111.21', 8000)
my_socket.bind(my_addr)

my_socket.listen()

# my_socket.accept()

client, addr = my_socket.accept()

data = client.recv(1024)
request = data.decode('utf8')
print(f"Got request from {addr}:\n{request}")

content = """
    <html>
        <head>
            <meta charset="utf-8">
            <title>OLOLOLOLOLOLOLOLO</title>
        </head>
        <body>
            <h1>Привет из мира Питон!</h1>
        </body>
    </html>

"""
http_head = f"""HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: {len(content)}
"""
responce = http_head + content 
client.send(responce.encode("utf8"))

client.close()