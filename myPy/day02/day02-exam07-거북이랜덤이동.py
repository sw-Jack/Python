import turtle as t
import random

t.shape("turtle")
t.speed(10)

for x in range(500) :
    num = random.randint(1,360)

    t.setheading(num)
    dist = random.randint(5,20)
    t.forward(dist)
