# 터틀런 게임

import turtle as t
import random

score = 0   # 게임 점수
playing = False     # 게임 실행중인지 여부

# 악당 거북이
te = t.Turtle()     
te.shape("turtle")
te.color("red")

te.speed(0)
te.up()
te.goto(0,200)

# 먹이
ts = t.Turtle()
ts.shape("circle")
ts.color("green")
ts.up()
ts.goto(0,-200)

# 방향키에 의한 방향 전환을 위한 함수들
def turn_right() :
    t.setheading(0)     # 오른쪽 : 0 / 위 : 90 / 왼쪽 : 180 / 아래 : 270

def turn_up() :
    t.setheading(90)

def turn_left() :
    t.setheading(180)

def turn_down() :
    t.setheading(270)

# 실제 게임을 진행하는 함수
def play() :
    global score
    global playing
    
    t.forward(10)

    if random.randint(1,5) == 3 :
        
        ang = te.towards(t.pos())
        te.setheading(ang)
        
    speed = score + 5
    if speed > 15 :
        speed = 15 
    te.forward(speed)

    # 악당 거북이와 나의 거리가 12보다 작으면 잡힌 것
    if t.distance(te) < 12 :
        text = "Score : " + str(score)
        message("Game Over!",  text)
        score = 0
        playing = False
        
    # 먹이와 나의 거리가 12보다 작으면 먹은 것
    if t.distance(ts) < 12 :
        score = score + 1
        t.write(score)
        star_x = random.randint(-230, 230)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)
        
    if playing :
        t.ontimer(play, 100)
        
# 게임을 시작하는 함수
def start() :
    global playing
    if playing == False :
        playing = True
        t.clear()
        play()
        
def message(m1,m2) :
        t.clear()
        t.goto(0,100)
        t.write(m1, False, "center", ("",20))
        t.goto(0,-100)
        t.write(m2, False, "center", ("",15))
        t.home()    # 원래 위치로



t.title("Turtle Run Game")
t.setup(500, 500)
t.bgcolor("orange")
t.shape("turtle")
t.speed(0)
t.up()
t.color("white")

t.onkeypress(turn_right, "Right")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run Game", "[Space]")
play()


