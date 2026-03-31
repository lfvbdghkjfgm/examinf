k = 1076
nums = [[int(i) for i in x.split()] for x in open('1.txt')]
data = []
for a,b,c,d,e in nums:
    data.append([b+c+d+e,e,a])
data.sort()
res = []
pol_res = []
def get_data(score):
    return [i for i in data if i[0] == score]

for i in range(320,0,-1):
    d = get_data(i)
    if len(d) < k:
        for i in d:
            res.append(i)
        k -= len(d)
    else:
        last_i = i
        break

print(get_data(280))
print(len(get_data(279)))