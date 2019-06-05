import turtle as t

def f(x):
    y = (x**2 + x - 1) * 0.01 #0.1은 너무 커서 0.01로 줄였습니다.
    t.goto(x, y)
    return 0

for a in range(4):
    t.circle(150, steps = 2)
    t.left(90)

t.penup()
f(-150)
t.pendown()

for i in range(-150, 151):
    f(i)

