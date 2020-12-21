# 타자 게임

import random
import time

w = ["cat","dog","fox","monkey","mouse","panda","giraff"]
n = 1
print("[타자 게임] 준비되면 엔터를 치세요!")
input()

start = time.time()
q = random.choice(w)
while n <= 5 :
    print(f'문제 {n} : {q}')
    x = input()
    if q == x :
        print("통과")
        n = n + 1
        q = random.choice(w)
    else :
        print("오타. 다시 도전!!")

end = time.time()
et = end - start
et = format(et, ".2f")
print(f'타자 시간 : {et}초')
