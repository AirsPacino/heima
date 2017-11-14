import os
import time

ret = os.fork()

if ret==0:
	print("--1--")
else:
	print("--2--")

ret = os.fork()
if ret==0:
	print("--11--")
else:
	print("--22--")

"""会打印两次11,22，一次1,2"""
"""n个fork，就会产生2^n个进程"""

"""fork炸弹"""
