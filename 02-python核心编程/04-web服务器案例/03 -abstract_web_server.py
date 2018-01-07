# coding:utf-8
# a webserver named MyServer

import socket

from multiprocessing import Process


class HTTPServer(object):
    """这里是关于这个类的注释"""
    """先不要去想要定义些什么，用的时候再想"""
    def __init__(self, port):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.server_sock.bind(("127.0.0.1", port))
        print("初始化完成!")


    def start(self):
        self.server_sock.listen(128)
        print("web server listening on port 8000...")
        while True:
            cli_sock, ser_info = self.server_sock.accept()
            handle_process = Process(target=self.handler, args=(cli_sock,))
            handle_process.start()
            cli_sock.close()


    def handler(self, cli_sock):

        HTML_ROOT_DIR = "."

        acp_data = cli_sock.recv(1024)
        print(acp_data)
        first_line = acp_data.splitlines()[0].decode("utf-8")

        print("the request file is:%s" % first_line.split(" ")[1])

        file_name = HTML_ROOT_DIR + first_line.split(" ")[1]

        if "./" == file_name:
            file_name = "./index.html"

        """
        try:
            fd = open(file_name, "rb")
        except IOError:
            print("file can not found!")
        """
        try:
            with open(file_name, "rb") as fd:
                file_data = fd.read()
                response_head = "HTTP/1.1 200 OK\r\n"
                response_server = "MyServer\r\n"
        except IOError:
            print("This file <%s> not found!" % file_name)

        """防止因为请求facivo.ico出现异常，图片二进制数据不可以解码"""
        if "./favicon.ico" == file_name:
            response = file_data
            cli_sock.send(response)
        else:
            response = response_head + response_server + "\r\n" + file_data.decode("utf-8")
            cli_sock.send(bytes(response, "utf-8"))

        cli_sock.close()


def main():
    """现在模拟这个类的用法"""
    """生成这个对象的时候应该就初始化好一些基本属性，要用到__init__方法"""
    http_server = HTTPServer(8000)

    """在这之前应该初始化好这个server对象的基本属性"""
    http_server.start()


if __name__ == '__main__':
    main()



