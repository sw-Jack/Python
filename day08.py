print("\n")
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
# 기본형
'''
from random import *
n1 = randint(10,99)
n2 = randint(10,99)
print("{} + {} = ".format(n1,n2), end='')    #### end 사용
user = int(input())
if user == n1+n2 :
    print("정답입니다")
else : 
    print("오답입니다")
'''
# 사용자 입력 input 안에서 한번에 입출력
'''
from random import *
n1 = randint(10,99)
n2 = randint(10,99)
userin = int(input('<문제>\n{} + {} = ? '.format(n1,n2)))
if userin == n1+n2 :
    print("{} 정답입니다!".format(userin))
else :
    print("틀렸습니다!")
'''

# 양수, 음수 판별
# if 만 사용하는 경우 조건식 만족 후 불필요한 코드 검사 -> elif 사용
'''
a = int(input("정수를 입력하세요 : "))
if a > 0 :
    print("양수입니다")
if a == 0 :
    print("0입니다")
if a < 0 :
    print("음수입니다")         
'''

# if ~ elif 문 
'''
a = int(input("정수를 입력하세요 : "))
if a > 0 :
    print("양수입니다")
elif a == 0 :
    print("0입니다")
elif a < 0 :
    print("음수입니다")   
'''

# if 만 사용
'''
a = 0
if a == 0 :
    print('안녕하세요1')
if a == 1 :
    print('안녕하세요2')
if a == 0 :
    print('안녕하세요3')       
'''

# if ~ elif 사용  
'''
a = 0
if a == 0 :
    print('안녕하세요1')
elif a == 1 :
    print('안녕하세요2')
elif a == 0 :
    print('안녕하세요3')   
'''
'''
a = 0
if a == 1 :
    print('안녕하세요0')
elif a == 0 :
    print('안녕하세요1')        
elif a == 0 :
    print('안녕하세요2')       # 안녕하세요1 만 출력
'''

# if ~ elif ~ else
'''
a = 0
if a == 1 :
    print('안녕하세요0')
elif a == 1 :
    print('안녕하세요1')        
elif a == 1 :
    print('안녕하세요2')      
else :
    print('안녕하세요3')       # 안녕하세요3 출력
'''

# if ~ elif 문
# elif 는 if 문을 사용할 때 여러개의 조건식을 사용하고 싶을 때 쓰는 문법입니다
# if 문의 조건식이 거짓일 경우 elif 의 조건식을 비교합니다
# elif 의 조건식에서 결과가 참(True)이면 더 이상 그 아래에 있는 문장을 실행하지 않습니다
# elif 는 독립적으로 사용할 수 없습니다 반드시 if 와 같이 사용해야 합니다
'''
a = 0
elif a == 0 :
    print("elif 는 독립적으로 사용 불가능")
'''
'''
wei = int(input("몸무게를 입력하세요 : "))
if wei >= 90 :
    print("비만입니다")
elif wei >= 70 :
    print("적정 체중입니다")
elif wei >= 50 :
    print("저체중입니다")         
'''

# 연습 문제
# 사용자에게 점수를 입력받아서 90점 이상이면 A
# 80점 이상 89점 이하 B
# 70점 이상 79점 이하 C
# 60점 이상 69점 이하 D
# 나머지 F
'''
score = int(input("점수 입력 : "))
if score >= 90 :
    print("A")
elif 80 <= score <= 89 :
    print("B")
elif 70 <= score <= 79 :
    print("C")   
elif 60 <= score <= 69 :
    print("D")
else :
    print("F")
'''
'''
score = int(input("점수 입력 : "))
if score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")   
elif score >= 60 :
    print("D")
else :
    print("F")                                      # elif 문 순서
'''

# while 반복문
# whlie 문은 if 문과 동일하게 조건식을 사용합니다
# 조건식의 결과가 참(True)이면 while 의 종속문장을 실행하고 거짓(False)이면 실행하지 않습니다
# while 은 종속 문장을 다 실행하면 다시 자신의 조건문을 비교합니다
# 조건식이 계속 참이면 반복문을 종료할 수 없고 그런 형태를 무한루프라고 합니다
# 사용 형식
'''
while 조건식 : 
    종속 문장1
    종속 문장2
'''
# 무한 루프
'''
a = 0
while a == 0 :
    print("Hello")    
'''
# 반복 횟수 설정
'''
a = 1
while a <= 10 :
    print("박수를 %d번 쳤습니다" %a)
    a = a + 1
'''

# 10개의 사과가 0이 될때 까지 출력
'''
app = 10
while app >= 0 :
    print("사과 {}개 남았습니다".format(app))
    app = app - 1            # app = app -1 / app -= 1 (O) , app-- (X)
'''

# 무한 루프 
# 변수, 양의 정수, 음의 정수, 문자열 등 .. 을 참으로 인식
'''S
a = 10
while a :
    print("Hello")
'''
'''
while 10 :
    print("Hello")
'''
'''
while 123 :
    print("Hello")
'''
'''
while -123 :
    print("Hello")
'''
'''
while 'python' :
    print("Hello") 
'''
# 0 만 거짓으로 인식
'''
a = 10
while 0 :
    print("0 만을 거짓으로 인식")
'''

# 연습 문제
# 사용자에게 단수를 입력받아서 해당하는 구구단만 출력할 수 있는 프로그램 작성
# 조건
# 사용자는 반드시 2 ~ 9 까지의 숫자만 입력합니다
# 다른 숫자를 입력하면 "잘못된 값입니다. 다시 입력하세요" 라는 문구가 나와야합니다
# 그리고 구구단 출력이 끝나면 다시 단수를 입력받는 문구가 실행이 되어야 합니다
'''
while 1 :
    a = 1
    num = int(input("\n단수 입력 : "))
    if num in range(2,10) :
        while a <= 9 :
            print("{} X {} = {}".format(num,a,num*a))
            a = a + 1
    else :
        print("잘못된 값입니다. 다시 입력하세요")
    user = input("\n(계속 : g, 프로그램 종료 : e)")
    if user == 'g' :
        continue
    elif user == 'e' :
        break
'''


while True : 
    userin = int(input("\n단수를 입력하세요 : "))
    num = 1
    if userin in range(2,10) :
        while num <= 9 :
            print("{} X {} = {}".format(userin,num,userin*num))
            num += 1
    else : 
        print("잘못된 값입니다. 다시 입력하세요")






