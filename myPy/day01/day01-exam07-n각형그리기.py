import turtle as t

# n각형 그리기

n = 8
t.color("purple")
t.begin_fill()
for x in range(n) :
    t.forward(50)
    t.left(360/n)
t.end_fill()
