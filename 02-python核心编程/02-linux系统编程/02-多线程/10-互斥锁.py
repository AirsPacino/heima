import threading
g_num = 0

mutex = threading.Lock()

def test1():
    global g_num
    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("test1 g_num=%d" %g_num)

def test2():
    global g_num

    for i in range(1000000):
        mutex.acquire()
        g_num += 1
        mutex.release()
    print("test2 g_num=%d" %g_num)

p1 = threading.Thread(target=test1)
p1.start()

p2 = threading.Thread(target=test2)
p2.start()

print("g_num=%d" %g_num)


