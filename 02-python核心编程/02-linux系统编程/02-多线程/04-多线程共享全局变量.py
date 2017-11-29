from threading import Thread
import time
g_num = 100

def test1():
    global g_num
    for i in range(3):
        g_num += 1
        time.sleep(1)
    print("test1 g_num=%d" %g_num)

"""多线程共享，所以没有多进程中的进程间通信"""
"""多线程共享的是全局变量，函数里面的变量不共享，即使两个线程同时执行一个函数"""

def test2():
    global g_num
    print("test2 g_num=%d" %g_num)


if __name__ == "__main__":
    t1 = Thread(target=test1)
    t1.start()

    t2 = Thread(target=test2)
    t2.start()