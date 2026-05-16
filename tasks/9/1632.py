# Solved by lfvbdghkjfgm
# https://lfvb.ru

res = 0

nums = [[int(i) for i in x.split()] for x in open('1')]

for a,x in enumerate(nums,1):
     p =  [i for i in x if x.count(i) >1 ]
     np = [i for i in x if x.count(i) ==1 ]
     if sum(x)%2 == 1 and sum(p) ** 2 > sum(np)**2 and p and np:
         res=  a
print(res)