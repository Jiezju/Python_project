def print_loop():
    # 打印偶数
    for i in range(0,100):
        if i % 2 == 0:
            print(i)
        
    sum = 0
    i = 0
    while i<=100:
        sum += i
        i += 1
    
    print(sum)
    
def guess(target=0):
    x = 1
    while x != target:
        x = int(input('Please input a num!'))
        if x > target:
            print('smaller')
        elif x < target:
            print('bigger')
        else:
            break

    print('Success')


def login():
    while True:
        name = str(input('please input your name!'))
        secret = str(input('please input your secret!'))

        if name == 'a' and secret == '1':
            break

        print('ERROR')

    print('Success!')


if __name__ == '__main__':
    print_loop()
    # guess(target=0)
    login()


