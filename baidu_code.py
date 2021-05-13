import random

all_raw_code =  ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
                 '0','1','2','3','4','5','6','7','8','9',
                 'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

res = ''
for i in range(8):
    index = random.randint(0, len(all_raw_code)-1)
    res += all_raw_code[index]

print(res)