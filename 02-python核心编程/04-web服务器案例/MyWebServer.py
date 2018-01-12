# coding:utf-8
"""定义了application()这个统一的入口，WSGI标准的接口"""
import socket
import sys

import MyFrameWork

from multiprocessing import Process


class HTTPServer(object):
    """这里是关于这个类的注释"""
    """先不要去想要定义些什么，用的时候再想"""

    def __init__(self, Application):
        self.server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.app = Application

    def bind(self, port):
        self.server_sock.bind(("127.0.0.1", port))

    def start(self):
        self.server_sock.listen(128)
        print("web server listening on port 8000...")
        while True:
            cli_sock, ser_info = self.server_sock.accept()
            handle_process = Process(target=self.handler, args=(cli_sock,))
            handle_process.start()
            cli_sock.close()

    def start_response(self, status, env):
        response_first_line = "HTTP/1.1 " + status + "\r\n"
        response_header = response_first_line
        for i in env:
            response_header += "%s: %s\r\n" % i

        self.response_header = response_header

    def handler(self, cli_sock):
        acp_data = cli_sock.recv(1024)
        print(acp_data)
        first_line = acp_data.splitlines()[0].decode("utf-8")
        print("the request file is:%s" % first_line.split(" ")[1])
        file_name = first_line.split(" ")[1]
        print("file_name is :%s" %file_name)

        env = {
            "PATH_INFO": file_name
        }

        response_body = self.app(env, self.start_response)
        response = self.response_header + "\r\n" + response_body
        cli_sock.send(bytes(response, "utf-8"))

        cli_sock.close()

if __name__ == '__main__':
    http_server = HTTPServer(MyFrameWork.app)
    http_server.bind(8000)
    http_server.start()