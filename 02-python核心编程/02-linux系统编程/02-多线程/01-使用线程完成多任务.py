import threading
import time

def test():
    print("---------")
    time.sleep(1)

for i in range(5):
    t = threading.Thread(target=test)
    t.start()