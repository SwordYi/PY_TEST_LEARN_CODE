import threading
from datetime import *
import time

def test(subTimes):
    time.sleep(1) #休眠1秒
    x = 0
    while(x == 0):
        print("I a testing code! " + str(subTimes) +", Time: " + str(datetime.now()))

def thd():
    Threads = []
    for i in range(2):
        t = threading.Thread(target=test,args=(i,))
        t.setDaemon(True) # 启用守护线程
        Threads.append(t)  # 添加线程
    for t in Threads:
        t.start() # 启动线程
    for t in Threads:
        t.join(2) # 阻塞2秒

if __name__ == "__main__":
    thd()
    print("Main end!")