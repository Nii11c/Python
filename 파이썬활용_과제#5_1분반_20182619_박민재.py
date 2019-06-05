import turtle as t
t.shape("turtle")
t.hideturtle();

x = (int)(t.textinput("중첩 원", "정수 입력:"))
y = 360/x

for i in range(x):
    t.circle(50)
    t.left(y)
