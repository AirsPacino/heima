# compelte code can be saw in web_server project


import socket
from multiprocessing import Process

# web-server, 就是处理 recv() & send()之间的数据
ser_info = ("127.0.0.1", 9999)
ser_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ser_sock.bind(ser_info)
ser_sock.listen(5)
print("Listening on port:9999...")

cli_sock = ser_sock.accept()

while True:
    p = Process(target=run, args=())
    p.start()
    cli_sock.close()

def run(cli_sock):
    f = open("test.txt", "w")
    while True:
       data =  cli_sock.recv(1024)
       if data:
           f.write(data)
       else:
           break
    f.close()

"""
    主要是对接收到的字符串进行处理
    对文件内容进行提取，取第一行
    HTTP / HTTP/1.1
"""

