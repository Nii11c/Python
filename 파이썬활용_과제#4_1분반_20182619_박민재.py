import random as r

user = input("가위,바위,보 >> ")
com = r.choice (['가위','바위','보'])

print('user >> ',user,' com >>',com)
if user==com:
    print("비겼습니다")
elif user=='가위' and com=='바위':
    print("사용자 패")
elif user=='가위' and com=='보':
    print("사용자 승;")
elif user=='바위' and com=='보':
    print("사용자 패")
elif user=='바위' and com=='가위':
    print("사용자 승;")
elif user=='보' and com=='가위':
    print("사용자 패")
elif user=='보' and com=='바위':
    print("사용자 승;")

import turtle as t
t.shape("turtle")
t.speed(0)

x = (int)(t.textinput("text","길이1"))
y = (int)(t.textinput("text","길이2"))
z = (int)(t.textinput("text","길이3"))

if (x**2)+(y**2)!=(z**2):
    t.write("직각삼각형이 아님")
else:
    t.forward(x)
    t.left(90)
    t.forward(y)
    t.home()
