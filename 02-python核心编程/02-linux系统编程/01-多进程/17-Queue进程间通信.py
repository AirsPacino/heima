from multiprocessing import Queue,Process
import time
import random

def write(que):
	for i in ["A", "B", "C"]:
		print("put %s to queue" %i)
		que.put(i)
		time.sleep(random.random())

def read(que):
	while True:
		if not que.empty():
			mes = que.get()
			print("get %s from queue" %mes)
			time.sleep(random.random())
		else:
			break

if __name__ == "__main__":
	q = Queue()
	pw = Process(target=write, args=(q,))
	pr = Process(target=read, args=(q,))
	pw.start()
	pw.join()
	pr.start()
	pr.join()

	print('')
	print("数据读写完成！")
