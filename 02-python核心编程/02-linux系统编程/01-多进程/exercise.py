from multiprocessing import Pool, Manager
import os, time, random

def writer(qe, li):
    print("reader(%s)启动" % os.getpid())
    for i in li:
        print("写入%s" %i)
        qe.put(i)
        time.sleep(random.random())

def reader(qe):
    print("writer(%s)启动" %os.getpid())
    for i in range(qe.qsize()):
        print("读出%s" %qe.get())
        time.sleep(random.random())


if __name__ == "__main__":
    print("主进程%s启动" %os.getpid())
    li = ["guoguo", "lisijia", "shenwanjun"]

    po = Pool(3)
    qe = Manager().Queue()

    """这是请求"""
    po.apply(writer, (qe, li))
    po.apply(reader, (qe,))

    po.close()
    po.join()



