import uuid

class Task:
    def __init__(self, func, *args, **kwargs):
        self.callable = func
        self.id = uuid.uuid4()
        self.args = args
        self.kwargs = kwargs

    def __str__(self): # 支持print
        return 'Task id: ' + str(self.id)

def my_func():
    print('This is a task test!')

if __name__ == '__main__':
    task = Task(func=my_func)
    print(task)