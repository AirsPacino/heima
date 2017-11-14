from multiprocess improt Process

def test():
	pass

p = Process(target=test)
p.start()

p.join()
p.terminate()

