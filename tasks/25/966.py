from itertools import product
res = []
for d1 in '123456789':
    for l in range(10):
        for s in product('123456789',repeat=l):
            s = ''.join(s)
            num = f'32{s}54{d1}123'
            if int(num) > 10**13:
                break
            if int(num) % 519 ==0:
                if len(num) % 2 == 0:
                    if sum(map(int,num[:len(num)//2])) ==sum(map(int,num[len(num)//2:])):
                        res.append([int(num),int(num) // 519])

for i in sorted(res):
    print(*i)