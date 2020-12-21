import turtle as t

#거북이 생성
t.shape("turtle")

#거북이 색깔 지정
t.color("red")

#펜 굵기 지정
t.pensize(5)


#삼각형 그리기
for x in range(3) :
    t.forward(100)
    t.left(120)

#사각형 그리기
t.color("green")
t.pensize(4)
for x in range(4) :
    t.forward(100)
    t.left(90)

#원 그리기
t.color("blue")
t.pensize(3)
t.circle(50)
t.forward(100)
t.circle(50)
