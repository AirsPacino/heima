from multiprocessing import Pool, Manager
import os, time

def reader(q):
    print("reader启动(%s), 父进程为(%s)" %(os.getpid(), os.getppid()))
    for i in range(q.qsize()):
        print("读出%s从队列" %q.get())

def writer(q):
    print("writer启动(%s), 父进程为(%s)")
    for i in "Pacino":
        print("写入%s到队列" %i)
        q.put(i)

if __name__ == "__main__":
    """父进程启动"""
    print("%s启动" %os.getpid())

    """队列是先进先出的"""
    q = Manager().Queue()

    """关于Pool，当有新的请求提交到Pool中时--------
       如果Pool没有满（即没有达到最大进程），就会创建新进程执行该请求
       如果Pool已经满了，那么这个请求就会被等待，知道进程池中有进程执行完成
    """
    po = Pool()

    """这是阻塞方式，一个进程执行完才会调用下一个进程"""
    """下面的就是请求..."""
    po.apply(writer, (q,))
    po.apply(reader, (q,))

    """po是进程池，po.close()就相当于进程池不再接受请求"""
    po.close()
    po.join()
    """主进程关闭"""
    print("(%s) End" %os.getpid())

