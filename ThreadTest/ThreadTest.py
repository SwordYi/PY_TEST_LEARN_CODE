import threading
from datetime import *

def test(subTimes):
    print("I a testing code! " + str(subTimes) +", Time: " + str(datetime.now()))

def looptest(mainTimes):
    for subTimes in range(20):
        test("Main Times: " + str(mainTimes) + ", Sub Times: " + str(subTimes))

def thd():
    Threads = []
    for mainTimes in range(25):
        Threads.append(threading.Thread(target=looptest,args=(mainTimes,)))  # 添加线程
    for t in Threads:
        t.start() # 启动线程

if __name__ == "__main__":
    thd()