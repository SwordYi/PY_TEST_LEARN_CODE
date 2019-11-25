import threading
from datetime import *
import time

THREAD_NUM = 1     # 线程数
ONE_WORKER_NUM = 1 # 每个线程执行的循环数

def test():
    # 测试代码
    pass

def working():
    global ONE_WORKER_NUM
    for i in range(0, ONE_WORKER_NUM):
        test()

def thd():
    global THREAD_NUM
    Threads = []
    for i in range(THREAD_NUM):
        t = threading.Thread(target=working, name="T" + str(i))
        t.setDaemon(True)  # 启用守护线程
        Threads.append(t)  # 添加线程
    for t in Threads:
        t.start() # 启动线程
    for t in Threads:
        t.join() # 阻塞线程

if __name__ == "__main__":
    thd()