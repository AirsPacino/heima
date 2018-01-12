import time

from MyWebServer import *

HTML_ROOT_DIR = "./html"


class Application(object):
    def __init__(self, urls):
        self.urls = urls

    def __call__(self, env, start_response):
        print(env)
        """字典的get方法"""
        path = env.get("PATH_INFO", "/")
        """/static/test.html"""
        if path.startswith("/static"):
            """try...except...else..."""
            try:
                f = open(HTML_ROOT_DIR + path[7:], "rb")
            except IOError:
                status = "404 not found "
                headers = []
                start_response(status, headers)
                return "not found"
            else:
                file_data = f.read()
                f.close()
                status = "200 OK"
                headers = []
                start_response(status, headers)
                return file_data.decode("utf-8")
        for url, whynot in self.urls:
            if url == path:
                print(whynot)
                status = "200 OK "
                headers = [
                    ("Content-type", "text/plain")
                ]
                start_response(status, headers)
                return whynot()


def show_time():
    return time.ctime()


def sayhello():
    return "hello Pacino!"

def readfile():
    try:
        f = open("MyWebServer.py", "rb")
    except IOError:
        f.close()
        return "file not found!"
    else:
        data = f.read()
        f.close()
        return data.decode("utf-8")


urls = [
    ("/ctime", show_time),
    ("/sayhello", sayhello),
    ("/readfile", readfile)
]

app = Application(urls)




"""这个不应该是主程序...."""
# if __name__ == '__main__':
#     """不要忽视任何一步，都是坑啊啊啊啊。。。。。。。 2018/1/11 23:47"""
#     urls = [
#         ("/ctime", show_time),
#         ("/sayhello", sayhello),
#         ("/readfile", readfile)
#     ]
#
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()
