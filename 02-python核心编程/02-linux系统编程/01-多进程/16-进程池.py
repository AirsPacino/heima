# Pool
# 需要创建的进程较多时
import os
from multiprocessing import Pool

def pool_handler(arg):
    for i in range(5):
        print("==pid=%d==arg=%d" %(os.getpid(), arg))

po = Pool(3)    """最多同时跑三个"""

"""向进程池添加任务，如果超过了进程池中进程的个数的话，依然可以添加"""
for i in range(10):
    print("--%d--" %i)
    Pool.apply_async(pool_handler, (i,))

"""相当于不能向进程池添加任务"""
po.close()
po.join()