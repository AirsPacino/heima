# coding:utf-8
import threading
import time

"""
    "大圣，此去欲何？"
    "踏南天，碎凌霄！"
    "若一去不回...?"
    "便一去不回！"
"""

count = 0
class HeritageThread(threading.Thread):
    def __init__(self, lock, thread_name):
        super(HeritageThread, self).__init__(name=thread_name)
        self.lock = lock

    def run(self):

        global count
        self.lock.acquire()

        for i in xrange(100):
            count = count + 1
            print("TheadName:%s count:%d" %(self.name, count))

        self.lock.release()


if __name__ == '__main__':
    mylock = threading.Lock()
    thread_name_list = ["N1", "N2", "N3"]
    for thread_name in thread_name_list:
        HeritageThread(mylock, thread_name).start()
    time.sleep(2)
