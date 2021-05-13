#原始数据，需要被处理的数据
friends=[
    ['张宇', '男', 24, '河北'],
    ['王丽娜','女',33, '陕西'],
    ['李萍', '女',28, '山东'],
    ['徐晴', '女',25, '四川'],
    ['马潇潇', '男', 34, '四川'],
    ['张晓', '男', 27, '陕西']
]


boy_list = []
girl_list = []
distric_list = []

age_big30 = []
biggest = []
smallest = []

def ansys(friends):
    bigger_age = 0
    small_age = 100
    for ele in friends:
        if ele[1] == '男':
            boy_list.append(ele)
        else:
            girl_list.append(ele)
        
        if ele[2] > bigger_age:
            biggest = ele
            bigger_age = ele[2]
        
        if ele[2] < small_age:
            smallest = ele
            small_age = ele[2]
        
        if ele[2] > 30:
            age_big30.append(ele)

        distric_list.append(ele[-1])

    print(boy_list)
    print(girl_list)
    print(distric_list)
    print(age_big30)
    print(biggest)
    print(smallest)
        

ansys(friends)
