import time

def count_time(func):
        	
    def improve_func():
        start_time = time.process_time()
        func()
        end_time = time.process_time()
        print('==============')
        print(start_time - end_time)
    
    return improve_func
        
@count_time # 装饰器 @闭包函数名
def print_odds():
    for i in range(100):
        if i % 2 == 1:
            print(i)

if __name__ == '__main__':
    print_odds()
    print_odds()