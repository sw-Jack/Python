import turtle as t

te = t.Turtle()     # 악당 거북이
te.shape("turtle")
te.color("red")
te.up()
te.goto(0,200)
te.down()

ts = t.Turtle()     # 내 거북이
ts.shape("turtle")
ts.color("green")


# ontimer(실행할함수, 정해진시간)
# ontimer(ts.got(100,-50), 1000)

ang = te.towards(ts.pos())
te.setheading(ang)
te.forward(10)      # 악당 거북이가 내 거북이 쪽으로 쫓아오는 상황

