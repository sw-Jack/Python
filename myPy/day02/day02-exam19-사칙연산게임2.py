# eval() : 문자열을 숫자로 취급할 수 있음
# eval("3+5")

import random

def make_question() :
    a = random.randint(1,50)
    b = random.randint(1,50)
    op = random.randint(1,3)

    q = str(a)

    if op == 1 :
        q = q + "+"
    if op == 2 :
        q = q + "-"
    if op == 3 :
        q = q + "*"

    q = q + str(b)

    return q

sc = 0 # 점수

for x in range(10) :
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans)

    if eval(q) == r :
        print("정답입니다.")
        sc = sc + 10
        
print("총 점수 : ", sc)

if sc == 100 :
    print("만점입니다.")








    
