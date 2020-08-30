print("\n")
# 비교 연산자
#1. ==
# a == b : a는 b와 같다
# a와 b의 값이 같을 경우 참(True)을 반환합니다

#2. != 
# a != b : a는 b와 같지 않다
# a와 b의 값이 같지 않을 경우 참(True)을 반환합니다

#3. <, >
# a > b : a가 b보다 크다
# a가 b보다 값이 큰 경우 참(True)을 반환합니다
# a < b : a가 b보다 작다
# a가 b보다 값이 작은 경우 참(True)을 반환합니다

#4. <=, >=
# a >= b : a가 b보다 크거나 같다
# a가 b보다 값이 크거나 같은 경우 참(True)을 반환합니다
# a <= b : a가 b보다 작거나 같다
# a가 b보다 값이 작거나 같은 경우 참(True)을 반환합니다


# 논리 연산자
#1. and 
# and 연산자는 왼쪽과 오른쪽에 있는 피연산자가 모두 참(True)일 경우에만 참(True)을 반환합니다
# 1 + 1 = 2 and 2 + 2 = 4
# print(True and True)
# 1 + 1 = 2 and 2 + 2 = 5
# print(True and True)
# print(True and False)
# print(False and True)
# print(False and False)

#2. or
# or 연산자는 두개의 피연산자 중 하나만 참(True)이면 참(True)을 반환합니다
# 1 + 1 = 2 or 1 + 1 = 3
'''
print(True or False)
print(False or True)
print(True or True)
print(False or False)
'''

#3. not
# not 연산자는 오른쪽 피연산자의 값이 참(True)이면 거짓(False)을 반환하고 거짓(False)이면 참(True)을 반환합니다
# not 1 + 1 = 2 
'''
print(not True)
print(not False)
print(not (True or False))
print(not (True and False))
'''

'''
x = 80 
if x > 10 and x < 100 : 
    print("x는 10보다 크고 100보다 작습니다")

x = 80
if 10 < x < 100 : 
    print("x는 10보다 크고 100보다 작습니다")
'''


# 멤버 연산자
#1. in
# 1 in (1,2,3)
# 왼쪽 피연산자의 값이 오른쪽 피연산자 멤버 중 일치하는 값이 있으면 참(True)을 반환합니다
'''
print(1 in (1,2,3))  # 튜플
print('가' in ['가','나','다'])  # 리스트
print(1 in (3,2,0))
'''
'''
print(1 in (1,2,3))  
print(20.2 in (20.1,20.2,20.3))
print('가' in ['가','나','다']) 

print(1 in (0,2,4))  
print(10.0 in (9.0,11.0,13.0))
print('요' in ['안','녕','하','시','오']) 
'''

#2. not in
# 1 not in (1,2,3)S
# 왼쪽 피연산자의 값이 오른쪽 피연산자 멤버 중 일치하는 값이 없으면 참(Ture)을 반환합니다
'''
print(1 not in (1,2,3))
print(1 not in (0,4,2))
print(1 not in [0,4,2])
'''
'''
print(1 not in (1,2,3))  
print(20.2 not in (20.1,20.2,20.3))
print('가' not in ['가','나','다']) 

print(1 not in (0,2,4))  
print(10.0 not in (9.0,11.0,13.0))
print('요' not in ['안','녕','하','시','오']) 
'''

# type()을 사용한 식별 연산자
#1. is
# 두 피연산자의 식별 값을 비교하였을 때 동일한 자료형이면 참(True)을 반환합니다
'''
a = 10
b = "파이썬"
print(type(a))             # a는 int, 정수형
print(type(a) is int)      # 참(True)
print(type(a) is float)    # 거짓(False)
print(type(a) == int)      # is 를 == 연산자로 대체할 수 있다.
print(type(a) == float)
print(type(b))
print(type(b) is str)      # b는 string, 문자열형
print(type(b) is chr)      # 거짓(False)
print(type(b) is int)      # 거짓(False)
'''

#2. is not
# 두 피연산자의 식별 값을 비교하였을 때 동일하지 않은 자료형이면 참(True)을 반환합니다
'''
a =  '가'
b = 100
print(type(a) is not str)    
print(type(a) is not float)   
print(type(a) != str)
print(type(a) != float)
print(type(b) is not int)
print(type(b) is not chr)
'''


# 연습 문제S
#1. 사용자에게 정수를 입력받아서 양수와 음수를 구별해주는 프로그램
# elif 사용할 경우
'''
num = int(input("정수 입력 : "))
if num > 0 : 
    print("양수")
elif num == 0 :
    print("양의 정수도 음의 정수도 아닙니다")
else :
    print("음수")
'''

# elif 사용하지 않을 경우 -> 앞에서 조건식을 만족하는 경우를 찾아도 계속해서 뒷 코드까지 검사 (비효율적)
'''
num = int(input("정수 입력 : "))
if num > 0 : 
    print("양수")
if num == 0 :
    print("양의 정수도 음의 정수도 아닙니다")
if num < 0 :
    print("음수")
'''


#2. 사용자가 식당에서 메뉴판을 보고 음식을 시키려고 합니다
# 사용자가 먹고 싶은 메뉴를 입력해서 음식이 메뉴에 포함되어 있으면 그 가격을 출력하는 프로그램
# 가격은 마음대로
'''(case1)
라면, 김밥, 만두 = 3000, 2500, 2000
menu = input("메뉴 입력  : ")
if menu in ('라면', '김밥', '만두') :
    if menu == '라면' :
        print("가격 : {}".format(라면))
    if menu == '김밥' :
        print("가격 : {}".format(김밥))
    if menu == '만두' :
        print("가격 : {}".format(만두))
else : 
    print("메뉴가 없습니다")
'''

'''(case2)
menu = ('라면','김밥','만두')
choi = input("메뉴 입력 : ")
if choi in menu :
    if choi == '라면' :
        print("2000원입니다")
    if choi == '김밥' :
        print("1000원입니다")
    if choi == '만두' :
        print("1500원입니다")
else :
    print("메뉴가 없습니다")
'''


#3. 사용자에게 정수를 입력받아서 짝수, 홀수를 구별하는 프로그램
'''
num = int(input("정수 입력 : "))
if num%2 == 0 :
    print("짝수")
else :
    print("홀수")
'''    


#4. 사용자로부터 2개의 정수 값을 입력받고 홀, 짝을 비교하였을때 
# 2개의 값이 전부 홀수 또는 짝수이면, 2개의 정수 값을 더하고
# 2개의 값이 홀-짝 또는 짝-홀이면, 2개의 정수 값을 곱하는 프로그램
'''
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
if num1%2 == num2%2 :
    print("두 수의 덧셈\n{} + {} = {}".format(num1,num2,num1+num2))
else :
    print("두 수의 곱셈\n{} * {} = {}".format(num1,num2,num1*num2))
'''


#5. 랜덤 함수를 통해 생성된 2개의 값 (10 ~99) 으로 
# 더하기 문제를 만들고 만들어진 문제를 사용자가 풀어보는 형식의 프로그램
'''
from random import *
n1 = randint(10,99)
n2 = randint(10,99)
csum = n1 + n2
userin = int(input('<문제>\n{} + {} = ? '.format(n1,n2)))
if userin == csum :
    print("{} 정답입니다!".format(userin))
else :
    print("틀렸습니다!")
'''


