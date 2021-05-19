#使用一个生成器生成抽奖ID
my_gen = (x for x in range(1,10000))

#参加抽奖的总人数 (注意这里是延伸的一个设计，一会儿我们讲为什么)
total_p = 30

#奖品字典 包含 奖品和奖品数量
prize_dict = {'iphone11':2,'ipad':3,'macbook':1,'switch':3,'京东500元购物卡':5,'PS4':2}


import random

#用于抽奖的列表，我们叫做抽奖池.奖池开始肯定是空的，根据我们实际情况添加
lottery_list = []

def probability(num_p, dic):
    # 添加奖品列表
    for k, v in dic.items():
        for i in range(v):
            lottery_list.append(k)
    
    for i in range(num_p - len(lottery_list[:])):
        lottery_list.append('no_prize')


probability(total_p, prize_dict)

random.shuffle(lottery_list)

print(lottery_list)

lottery_list_iter = iter(lottery_list)

# 抽奖
while True:
    if total_p > 0:
        if input() == 'Start':
            prize = next(lottery_list_iter)
            total_p -= 1
            if prize != 'no_prize':
                prize_id = format(next(my_gen), '04d')
                print(prize + ' ' + str(prize_id))
            else:
                print('Sorry' + ' ' + prize)
        elif input() == 'End':
            break
    else:
        print('Sorry, no more choice!')
        break

