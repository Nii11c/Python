print("이름 첫째자는 >>")
name1 = input()
print("이름 둘째자는 >>")
name2 = input()
print("이름 셋째자는 >>")
name3 = input()

c = len(name1)+len(name2)+len(name3)

print('*' * c) #별출력

print(name2[0]+name3[0]+name1) #바꾼이름출력

import turtle as t
t.shape('turtle')

t.penup()
t.write("STOP")
t.goto(-12.5, -35) #거북이 이동
t.pendown()
t.right(30)
t.circle(50, steps = 6) #육각형
t.hideturtle()#거북이숨김
