import psutil
import threading

from queue import ThreadSafeQueue
from task import Task, AsyncTask

# 单个线程的封装
class ProcessThread(threading.Thread):
    def __init__(self, task_queue, *args, **kwargs):
        threading.Thread.__init__(self, *args, **kwargs)
        # 创建事件管理标记： 
        # event.wait  调用该方法的线程会被阻塞 
        # event.set() 将event的标志设置为True  
        # event.clear() 将event的标志设置为False
        # event.is_set(） 判断event的标志是否为True
        self.dismiss_flag = threading.Event()
        self.task_queue = task_queue
        self.args = args
        self.kwargs = kwargs

    def run(self):
        while True:
            if self.dismiss_flag.is_set():
                break

            task = self.task_queue.pop()
            if not isinstance(task, Task):
                continue

            result = task.callable(*task.args, **task.kwargs)

            if isinstance(task, AsyncTask):
                task.set_result(result)

    def dismiss(self):
        self.dismiss_flag.set()

    def stop(self):
        self.dismiss()

# 线程池
class ThreadPool:
    def __init__(self, size=0):
        if not size:
            size = psutil.cpu_count() * 2 # 约定线程池的大小为CPU核数的两倍（最佳实践）
        
        self.pool = ThreadSafeQueue(size)
        self.task_queue = ThreadSafeQueue()

        for i in range(size):
            self.pool.put(ProcessThread(self.task_queue))

    # 启动线程池
    def start(self):
        # 启动每个线程
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.start()

    # 停止线程池
    def join(self):
        for i in range(self.pool.size()):
            thread = self.pool.get(i)
            thread.stop()
        
        while self.pool.size():
            thread = self.pool.pop()
            thread.join()

    # 线程池提交任务
    def put(self, item):
        if not isinstance(item, Task):
            raise TaskTypeErrorException()
        
        self.task_queue.put(item)

    def batch_put(self, item_list):
        if not isinstance(item_list, list):
            item_list = list(item_list)
        
        for item in item_list:
            self.put(item)

    def size(self):
        return self.pool.size()

class TaskTypeErrorException(Exception):
    pass