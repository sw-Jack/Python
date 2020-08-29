print("\n")
# 변수의 사용 형식
#1. 변수명 = 값
# a = 10
# print(a)
# name = '파이썬'
# print(name)

#2. 변수명1, 변수명2 = 값1, 값2S
# a, b = 10, 20
# print(a,b)
# num, name, age = 1, '강감찬', 26
# print(num,name,age)

#3. 변수명1 = 변수명2 = 값1
# a = b = 10
# print(a)
# print(b)
# math = eng = kor = 100 
# print(math);print(eng);print(kor)

# 변수 생성시 작명 규칙
#1. 알파벳, 숫자, 언더스코어(_)로 구성합니다

#2. 알파벳은 대소문자를 구분합니다\
# 대문자 A와 소문자 a는 완전히 다른 변수입니다
# a = 10
# A = 20
# print('a : {}, A : {}'.format(a,A))

#3. 변수명의 시작은 숫자로 시작할 수 없습니다
# 2a = 10
# print(2a)

#4. 숫자가 변수명의 시작이 아니라면 사용할 수 있습니다
# a2 = 10
# num10 = '파이썬'
# print(a2)
# print(num10)


#5. 공백이나 특수 문자는 변수의 이름에 포함될 수 없습니다
# a a = 10
# python!p = 10
# print(a a)
# print(python!p)

#6. 변수명은 한글로 사용 가능합니다
# # 국어, 영어, 수학 = 90, 100, 75
# print(국어,영어,수학)

# 변수의 자료형 확인
# type 함수는 type(x) 형식으로 사용하며 x값의 자료형을 보여주는 함수입니다
# a = 80;b = 80.0;c = "80"
# Integer 는 10진수 정수 형태의 자료형입니다
# print(type(a))  # Integer or int
# Float 는 실수 형태의 자료형입니다
# print(type(b))  # float
# String 은 문자열 형태의 자료형입니다
# print(type(c))  # String or str

# 변수의 형태 변환 (강제 형식 변환) -> 일시적 변환
# x, y, z = 10, 10.0, "10"
# print(x+y)
# print(x+int(z))       # 강제 형 변환 (z : 문자열형 -> 정수형) 
# print(str(x)+z)       # 강제 형 변환 (x : 정수형 -> 문자열형)
# print(x+float(z))     # 강제 형 변환 (z : 문자열형 -> 실수형)
# print(str(y)+z)       # 강제 형 변환 (y : 실수형 -> 문자열형)
# print(str(x)+str(y))  # 강제 형 변환 (x : 정수형 -> 문자열형)
                        # 강제 형 변환 (y : 실수형 -> 문자열형)

# 강제 형식 변환 후 변수에 초기화
# x, y, z ='1', 1, 1.0
# x, y, z = int(x), f
# float(y), str(z)
# print(type(x),type(y),type(z))

# 변수 연습 문제
# 출력 결과 
# 국어 : 87, 수학 : 66, 영어 : 90 일때, 총점 : ?, 평균 : ?
# [조건] : 변수 5개를 사용해서 표현
'''
(case 1)
kor, math, eng = 87, 66, 90
sum = kor + math + eng
avg = sum / 3
print("국어 : %d점" %kor)
print("수학 : %d점" %math)
print("영어 : %d점" %eng)
print("총점 : %d점, 평균 : %d점" %(sum,avg))

(case 2)
kor, math, eng = 87, 66, 90
sum = kor + math + eng
avg = sum / 3
# print('국어 : {}점'.format(kor))
# print('수학 : {}점'.format(math))
# print('영어 : {}점'.format(eng))
# print('총점 : {}점, 평균 : {}점'.format(sum,avg))
'''

# 변수 형식 변환 연습 문제
# x,y,z = '100',10.5,20
#1. 110.5 출력
#2. 10020 출력
#3. 10.520.0 출력
#4. 110.520 출력
'''
x,y,z = '100',10.5,20
print(int(x)+y)
print(x+str(z))
print(str(y)+str(float(z)))
print(str(int(x)+y)+str(z))
'''

# 사용자 입력 함수 (input)
# 표준 입력 함수
# input 함수를 사용하면 사용자가 직접 변수에 들어갈 값을 입력할 수 있습니다
# 키보드를 사용하여 변수에 들어갈 값을 입력합니다
# 사용 형식
# 변수명 = input()
# name = input()
# age = input()
# print("{}님의 나이는 {}세입니다".format(name,age))

# input() 안에 문자열을 입력하면 입력 값을 받을 때 input() 안에 적은 문자열도 같이 출력됩니다
# 입력은 문자열이 끝난 후 받습니다
# a = input('정수를 입력하세요 : ')
# print("a의 값은 {}입니다".format(a))
# name = input("이름은 입력하세요 : ")
# age = input("나이를 입력하세요 : ")
# print("{}님의 나이는 {}세입니다".format(name,age))

# input() 함수는 기본적으로 입력 값을 문자열로 인식합니다
# ex1 = input()
# ex2 = input()
# print("{} + {} = {}".format(ex1,ex2,ex1+ex2)) 
 
'''
a = input("정수를 입력하세요 : ")
b = input("정수를 입력하세요 : ")
print(int(a)+int(b))  # 형 변환은 일시적
print(a+b)            # 형 변환 이전 값이 다시 출력
'''
# input() 함수 자체를 형 변환으로 받는다
'''
a = int(input("정수를 입력하세요 : "S))
b = int(input("정수를 입력하세요 : "))
print(a+b)
'''

ex1 = float(input("실수를 입력하세요 : "))
ex2 = int(input("정수를 입력하세요 : "))
print(ex1+ex2)
print(ex1-ex2)
print(ex1*ex2)
print(ex1/ex2)

































