import turtle as t

#변수 생성
dist = 100 #변수 dist에 100이라는 값을 저장

#거북이 생성
t.shape("turtle")

#거북이 색깔 지정
t.color("red")

#펜 굵기 지정
t.pensize(5)


#삼각형 그리기
t.forward(dist)
t.left(120)
t.forward(dist)
t.left(120)
t.forward(dist)
t.left(120)

#사각형 그리기
t.color("green")
t.pensize(4)
t.forward(dist)
t.left(90)
t.forward(dist)
t.left(90)
t.forward(dist)
t.left(90)
t.forward(dist)
t.left(90)

#원 그리기
t.color("blue")
t.pensize(3)
t.circle(50)
t.forward(dist)
t.circle(50)
