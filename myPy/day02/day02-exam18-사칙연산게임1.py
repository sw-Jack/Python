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

sc1 = 0 # 정답 갯수
sc2 = 0 # 오답 갯수

for x in range(5) :
    q = make_question()
    print(q)
    ans = input("=")
    r = int(ans)

    if eval(q) == r :
        print("정답입니다.")
        sc1 = sc1 + 1
    else :
        print("오답입니다.")
        sc2 = sc2 + 1
print("정답 : ", sc1, ", 오답 : ", sc2)

if sc2 == 0 :
    print("만점입니다.")








    
