import threading
import uuid

class Task:
    def __init__(self, func, *args, **kwargs):
        self.callable = func
        self.id = uuid.uuid4()
        self.args = args
        self.kwargs = kwargs

    def __str__(self): # 支持print
        return 'Task id: ' + str(self.id)

class AsyncTask(Task):
    def __init__(self, func, *args, **kwargs):
        super().__init__(func, *args, **kwargs)
        self.result = None
        self.condition = threading.Condition()

    def set_result(self, result):
        self.condition.acquire()
        self.result = result
        self.condition.notify()
        self.condition.release()

    def get_result(self):
        self.condition.acquire()
        if not self.result:
            self.condition.wait()
        result = self.result
        self.condition.release()
        return result


def my_func():
    print('This is a task test!')

if __name__ == '__main__':
    task = Task(func=my_func)
    print(task)