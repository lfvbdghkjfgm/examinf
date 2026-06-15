# Solved by lfvbdghkjfgm
# https://lfvb.ru

data = [[int(i) for i in x.split()] for x in open(r"C:\Users\aatop\Downloads\26.txt")]

students = {}

for student, task in data[1:]:
    if student not in students.keys():
        students[student] = set()
    if task % 2 == 0:
        students[student].add(task)

print(
    min([a for a, b in students.items() if b == max(students.values(), key=len)]),
    len(max(students.values(), key=len)),
)
