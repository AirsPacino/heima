from multiprocessing import Process
import time

class Process_class(Process):
	# def __init__(self):
	# 	pass

	def run(self):
#while True:
		for i in range(5):
			print("--1--")
			time.sleep(1)

p = Process_class()
p.start()
p.join()
