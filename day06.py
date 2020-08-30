print("\n")
# 연습 문제
#1. 사용자의 나이와 이름을 입력 받아서 출력하는 프로그램
# ex) 홍길동 님의 나이는 20살입니다.

# name = input("이름을 입력하시오 : ")
# age = int(input("나이를 입력하시오 : "))
# print("{}님의 나이는 {}살입니다".format(name,age))


# #1. 다른 표현 : split() 함수
# split() 함수를 사용하면 input() 하나로 여러개의 변수에 문자열 값을 지정할 수 있습니다
# split() 안에 아무것도 적지 않으면 띄어쓰기를 기준으로 값을 구분합니다 
# split() 안에 문자열을 입력하면 그 문자열을 기준으로 문자열을 구분합니다
# split() 은 문자열을 구분할 때 사용하기 때문에 int나 float 형태일 경우 사용할 수 없습니다 
'''
name, age = input("이름과 나이를 입력하세요").split() 
age = int(age)
print("{}님의 나이는 {}살입니다".format(name,age))
'''
'''
a = "안,녕,하,세,요"
print(a.split(','))
'''


#2. 사용자에게 2개의 정수를 입력 받아서 +,-,*,/ 결과가 모두 출력이 되도록 하는 프로그램
'''
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
print("%d + %d = %d" %(num1,num2,num1+num2))
print("{} - {} = {}".format(num1,num2,num1-num2))
print("%d X %d = %d" %(num1,num2,num1*num2))
print("{} / {} = {:.1f}".format(num1,num2,num1/num2))
'''
'''
num1, num2 = input("정수 2개를 입력하세요 : ").split()
num1 = int(num1)
num2 = int(num2)
print("%d + %d = %d" %(num1,num2,num1+num2))
print("{} - {} = {}".format(num1,num2,num1-num2))
print("%d X %d = %d" %(num1,num2,num1*num2))
print("{} / {} = {:.1f}".format(num1,num2,num1/num2))
'''

#3. 사용자가 직접 국어, 수학, 영어 점수를 입력해서 그 점수를 기준으로 총점과 평균을 출력하는 프로그램
'''
kor = int(input("국어 점수 입력 : "))
math = int(input("수학 점수 입력 : "))
eng = int(input("영어 점수 입력 : "))
sum = kor + math + eng
avg = sum / 3
print("국어 점수 : %d" %(kor))
print("수학 점수 : {}".format(math))
print("영어 점수 : {}".format(eng))
print("총점 : %d, 평균 : %.1f" %(sum,avg))
'''


# random() 함수-> random() 
'''
from random import random  -> 함수 사용 선언문 (모듈)
print(random())  # 0.0 초과 1.0 미만의 값이 무작위로 출력
print(random()*10)  # 0.0 초과 10.0 미만의 값이 무작위로 출력
print(int(random()*10))  # 0 ~ 9 의 값이 무작위로 출력
print(int(random()*10+1))  # 1 ~ 10 
print(int(random()*10+3))  # 3 ~ 12
'''

# randint() 함수
'''
from random import randint
print(randint(1,10))  # 1 ~ 10 의 값 무작위로 출력
print(randint(100,200))  # 100 ~ 200 의 값 무작위로 출력
print(randint(1,500))  # 1 ~ 500 의 값 무작위로 출력
'''
'''
from random import randint
print(chr(randint(65,90)))  # A ~ Z 의 문자 무작위로 출력
print(chr(randint(97,122)))  # a ~ z 의 문자 무작위로 출력
'''

# randrange() 함수
'''
from random import randrange
print(randrange(5,10))  # 5 이상 10 미만의 값이 무작위로 출력
print(randrange(1,1000))  # 1 이상 10000 미만의 값이 무작위로 출력
print(randrange(1,10,2))  # 1 부터 2 씩 증가된 값에 대해 10 미만까지 출력
print(randrange(10,100,20))  # 10 부터 20 씩 증가된 값에 대해 100 미만까지 출력
'''

# random 이라는 모듈화되어 있는 파이썬 파일에 있는 모든 함수를 사용할 수 있습니다 (*)
'''
from random import * 
print(random())
print(randint(1,2))
print(randrange(1,5))
'''

# 제어문 if (조건문)
# if 조건문은 조건식의 결과에 따라서 값을 제어할 수 있게 해주는 문법입니다
# if는 조건식이 참(True) 일 경우에 종속 문장을 실행합니다
# if는 조건식이 거짓(False) 일 경우 종속 문장을 실행하지 않습니다
# 종속문장을 사용할 때 반드시 들여 쓰기(공백 4번)를 해야 정상적으로 사용이 가능합니다
# 사용 형식
'''
if 조건식 :
    종속 문장1
    종속 문장2
'''
'''
a = 10
if a == 10 :    
    print("a는 10입니다")
'''

# if ~ else 
# else 를 사용하면 if의 조건식이 거짓일 경우 else 아래에 있는 종속 문장을 실행합니다
# if 아래에 있는 종속 문장을 실행하지 않으면 반드시 if 와 else 둘 중 하나만 실행됩니다
# else 는 독립적으로 사용이 불가능하며 반드시 if 와 함께 사용되어야 합니다
# else 는 조건식이 필요없습니다
# 사용 형식
'''
if 조건식 :
    종속 문장1
else : 
    종속 문장2
'''
'''
ex1 = int(input("정수를 입력하시오 : "))
if ex1 == 9 : 
    print("ex1는 9입니다")
else : 
    print("ex1 는 9가 아닙니다")
'''

# 연습 문제
# 사용자에게 점수를 입력 받아서 80점 이상이면 합격, 미만이면 불합격이라는 결과가 나오는 프로그램
'''
score = int(input("점수를 입력하시오 : "))
if score >= 80 :
    print("합격")
else : 
    print("불합격")
'''

# 윤년 구하기
'''
year = int(input("연도를 입력하시오 : "))
if year%4 == 0 : 
    if year%100 == 0 :
        if year%400 == 0 :
            print("{}년은 윤년".format(year))
        else :
            print("{}년은 평년".format(year))
    else :
        print("{}년은 윤년".format(year))
else : 
    print("{}년은 평년".format(year))
'''
