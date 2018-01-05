import socket


# web-server, 就是处理 recv() & send()之间的数据
ser_info = ("127.0.0.1")
ser_sock = socket.socket()
ser_sock.bind(ser_info)

while True:
    p =


