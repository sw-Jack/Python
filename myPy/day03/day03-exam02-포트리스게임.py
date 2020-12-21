# 포트리스 게임

import turtle as t
import random

def turn_up() : # 방향키 위
    t.left(2)
def turn_down() :
    t.right(2) # 방향키 아래
def fire() :
    ang = t.heading()
    while t.ycor() > 0 :
        t.forward(15)   # 포물선 형성
        t.right(5)
    d = t.distance(target, 0)
    t.sety(random.randint(10,100))
    if d < 5 :
        t.color("blue")
        t.write("Good!", False, "center", ("", 15))
        t.color("black")
        t.goto(-200, 10)
        t.setheading(20)
    else :
        t.color("red")
        t.write("Bad!", False, "center", ("", 15))
        t.color("black")
        t.goto(-200, 10)
        t.setheading(ang)

# 땅 그리기
t.goto(-300,0)
t.down()
t.goto(300,0)

# 목표 지점 설정하고 그리기
target = random.randint(50,150)
t.pensize(3)
t.color("green")
t.up()
t.goto(target-25, 2)
t.down()
t.goto(target+25, 2)

# 거북이를 검은색으로 하고 처음 발사했던 곳으로 돌아감
t.color("black")
t.up()
t.goto(-200, 10)
t.setheading(20)

# 이벤트 설정
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(fire, "space")
t.listen()





































