import turtle
t=turtle.Turtle()
t.shape("turtle")

number = int(input("세자리 정수 입력: "))

n1 = number//100 #100의 자리
n2 = (number-(n1*100))//10 #10의 자리
n3 = (number-(n1*100)-(n2*10))//1 #1의 자리
n4 = (n3*100)+(n2*10)+n1 #역수

print("입력한 수의 역: ",n4)

length = int(input("원의 지름 입력: "))
halfL = length//2 #반지름 계산
x=(halfL)*(2**0.5) #정사각형의 대각선 길이 계산

t.circle(halfL) #원 그리기
t.forward(halfL)
t.left(45)
t.circle(x, steps=4) #정사각형 그리기
t.right(45)
