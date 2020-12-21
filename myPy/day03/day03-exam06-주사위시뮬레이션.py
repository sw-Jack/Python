# 주사위 시뮬레이션
import random

total = 1000000
ev = 0

for i in range(total) :
    x = random.randint(1,6)
    
    if x == 2 :
        ev = ev + 1
print(ev)
print(ev / total)

