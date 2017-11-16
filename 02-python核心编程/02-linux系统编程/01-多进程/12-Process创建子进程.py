from multiprocessing import Process
import time

def test():
	while True:
		print("hello")
		time.sleep(1)

# 有问题
#if __name__ == "__main__":
p = Process(target=test)
p.start()

while True:
	print("hh main")
	time.sleep(1)
