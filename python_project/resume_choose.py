#系统运行的基本配置
requirement=(('本科','硕士','博士'),30,('985','211'))

#系统的所需要处理的数据
list_all=[  #为什么这么搭配？ 列表套元组？？？
    tuple(['张晓','男',35,'本科','211']), #1.每个人的数据不可修改 因为这个是事实存在的
    tuple(['冯宇','男',24,'本科','双非']), #2.但是，有可能添加更多的人
    tuple(['王丽娜','女',28,'本科','985']),
    tuple(['李萍','女',26,'专科','双非']), #注意这个数据 专科
    tuple(['徐晴','女',25,'专科','双非']), #注意这个数据 专科
    tuple(['马潇潇','女',29,'硕士','211']),
    tuple(['张晓','男',27,'硕士','双非']),
    tuple(['李青青','女',31,'博士','非']),
    tuple(['刘星','男',24,'本科','985']),
    tuple(['乔斌','男',30,'硕士','双非'])
]

#准备好我们需要append数据的列表，用于保存筛选后的数据

resume_list=[] #简历库列表
choose_list=[] #候选列表
interview_list=[] #面试列表


for resume in list_all:
    if resume[3] in requirement[0]:
        resume_list.append(resume)

        if resume[2] < requirement[1]:
            choose_list.append(resume)
    
            if resume[-1] in requirement[-1]:
                interview_list.append(resume)

print(resume_list)
print()
print(choose_list)
print()
print(interview_list)