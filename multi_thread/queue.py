import time
import threading

class ThreadSafeQueue:
    def __init__(self, max_size=0):
        self.queue = []
        self.max_size = max_size
        self.lock = threading.Lock() # 创建锁对象
        self.condition = threading.Condition() # 创建条件变量对象

    def size(self):
        self.lock.acquire() # 上锁
        size  = len(self.queue)
        self.lock.release() # 解锁
        return size

    def put(self, item):
        if self.max_size != 0 and self.size() > self.max_size:
            return ThreadSafeQueueExceotion()

        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()
        self.condition.acquire() # 获取条件变量
        self.condition.notify()  # 唤醒其他线程
        self.condition.release() # 释放条件变量

    def batch_put(self, items):
        if not isinstance(items, list):
            items_list = list(items)

        for item in items_list:
            self.put(item)

    def pop(self, block=True, timeout=None):
        if self.size() == 0:
            if block:
                self.condition.acquire() # 获取条件变量
                self.condition.wait(timeout=timeout) # 等待条件变量唤醒
                self.condition.release() # 释放条件变量

            else:
                return None

        self.lock.acquire()
        item = None
        if len(self.queue) > 0:
            item = self.queue.pop()
        self.lock.release()
        return item

    def get(self, index):
        self.lock.acquire()
        item = self.queue[index]
        self.lock.release()
        return item

class ThreadSafeQueueExceotion(Exception):
    pass



def producer(string):
    while True:
        print(string)
        queue.put(1)
        time.sleep(3)

def consumer():
    while True:
        item = queue.pop(block=True, timeout=5)
        print('get item from queue: %d' % item)
        time.sleep(1)

queue = ThreadSafeQueue(100)

if __name__ == '__main__':
    thread1 = threading.Thread(target=producer,args=('hello producer',)) # 创建线程
    thread2 = threading.Thread(target=consumer)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()