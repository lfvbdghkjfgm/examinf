nums = [[int(i) for i in x.split()] for x in open('1.txt')]
nums = nums[1:]
data = []
for i,dt in enumerate(nums,1):
    data.append([dt[0],i,0])
    data.append([dt[1],i,1])
data.sort()

start = 0
end = -1

rating = [0] * len(nums)
last_place = 0

for a,b,c in data:
    if b in rating:
        continue
    if c == 0:
        rating[start] = b
        start += 1
        last_place = b
    elif c == 1:
        rating[end] = b
        end -= 1
        last_place = b
print(last_place,rating.index(last_place))
