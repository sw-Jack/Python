import turtle as t

t.shape("turtle")
t.pos() # 거북이 좌표(x,y)

t.forward(100)
t.pos()

a = t.xcor() # x좌표
b = t.ycor() # y좌표 

t.goto(50,50) # 특정 좌표로 이동
t.setx(-50) # x좌표 값 조정
t.sety(-50) # y좌표 값 조정
t.pos()

t.distance(100,100) # 현재 위치와 (100,100)의 거리


t.heading()


t.towards(10,10) # 현재 위치에서 (10,10)을 바라보는 각도

t.setheading(45) # 거북이 머리 각도 조정
t.forward(50)
t.home()

# 이벤트 설정(함수)
def f() :
    t.forward(10)

t.onkeypress(f, "Up")
t.onscreenclick(t.goto)
t.listen()
t.title("Welcome") # 창 제목 설정
t.write("Hello")
t.write("Hello", False, "center", ("",20))


