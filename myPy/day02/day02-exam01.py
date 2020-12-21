import turtle as t

n = int(input("숫자 입력 : "))

t.bgcolor("black")
t.color("red")
t.speed(1)
for x in range(n) :
    t.circle(80)
    t.left(360/n)

