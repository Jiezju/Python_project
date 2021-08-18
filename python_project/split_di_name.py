raw = [
    'http://www.baidu.com/index.html',
    'http://www.baidu.com/1.html',
    'http://post.baidu.com/index.html',
    'http://mp3.baidu.com/index.html',
    'http://www.baidu.com/3.html',
    'http://post.baidu.com/2.html',
]

dic = {}

for s in raw:
    tmp = s.split('/')
    #print(tmp[2])
    if tmp[2] not in dic:
        dic[tmp[2]] = 1
    else:
        dic[tmp[2]] += 1

max_count = 0
max_string = ''

for key,val in dic.items():
    if val > max_count:
        max_count = val
        max_string = key

print(max_string)