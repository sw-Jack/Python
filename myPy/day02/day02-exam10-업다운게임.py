
import random

n = random.randint(1,200)
print(n)

cnt = 0
while True :
    cnt += 1
    x = int(input("맞춰보세요 : "))

    if x == n :
        print("정답")
        break
    if x < n :
        print("너무 작아요")
    if x > n :
        print("너무 커요")
    if cnt >= 4 :
        print("실패")
        break

