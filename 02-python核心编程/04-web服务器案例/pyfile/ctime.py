import time

"""总之，这个接口函数就是用来处理响应的所有信息的"""
def application(env, start_respond):
    #状态码
    status = "200 OK"

    # 用户自己的环境信息
    headers = [
        ("pyresponse", "hello"),
        ("content-type", "text/html"),
        ("test", "test"),
        ("arbitry", "I think yes")
    ]

    """传入的请求用户的环境信息，模块自己本身的环境信息"""
    """这里汇总到一起，就是所有的头信息（除了第一行）"""
    headers += env

    """通过调用函数start_respond来得到状态码和响应头，return只能返回执行结果"""
    start_respond(status, headers)
    """规定必须有一个返回值, 返回执行结果"""
    return time.ctime()
