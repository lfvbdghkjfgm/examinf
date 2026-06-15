# Solved by Владимир Д.


from turtle import done, dot, down, fd, lt, pendown, rt, setpos, tracer, up

pendown()
lt(90)
tracer(0)
k = 10

for i in range(3):
    fd(11 * k)
    rt(90)
    fd(24 * k)
    rt(90)

up()

fd(2 * k)
rt(90)
fd(5 * k)
lt(90)
down()

for i in range(3):
    fd(6 * k)
    lt(90)
    fd(9 * k)
    lt(90)


up()
for x in range(-50, 50):
    for y in range(-50, 50):
        setpos(x * k, y * k)
        dot(3)


done()
