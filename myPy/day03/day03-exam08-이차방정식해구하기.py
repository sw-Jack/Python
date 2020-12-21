# 이차 방정식 : 근의 공식
# ax^2 + bx + c = 0 [a != 0]

# 판별식 : D = b^2 - 4ac
# D > 0 : 근이 두개 일때

# x = -b +- 루트(b^2 - 4ac) / 2a
# D = 0 : 근이 한개 일때

# x = -b / 2a
# D < 0 : 근이 없을때


import math
import sys

print("ax^2 + bx + c = 0")


# a, b, c를 입력받고 입력받은 문자열을 소수로 변경
a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

if a == 0 :
    print("a = 0 : 이차방정식이 아닙니다.")
    sys.exit()  # 프로그램 종료
    
D= b*b - 4*a*c  # 판별식
if D > 0 :
    x1 = (-b + math.sqrt(D))/(2*a)
    x2 = (-b - math.sqrt(D))/(2*a)
    print("2개의 해 : ", x1, " ", x2)
if D == 0 :
    x = -b / 2*a
    print("1개의 해 : ", x)
if D < 0 :
    print("해가 없습니다.")
