print()
# 전역 변수 (광역변수)
# 전역 변수 global을 사용하면 더 이상 함수 안에서만 사용하는 것이 아닌 함수 밖에 있는 변수를 사용한다는 뜻입니다
'''
a = 0
def test() :
    a = 0
    a = a + 1
test()
print(a)          # 변수 a의 값은 함수 안의 a 값 관계없이 함수 밖에서 선언된 전역 변수 a값으로 유지
'''

'''
a = 0
b = 1
def test() :
    global a      # 전역 변수 선언 : 함수 밖에 선언되어 있는 전역 변수에 영향을 줌
    global b
    a = a + 1
    b = b * 9
test()
print(a);print(b)
'''


# 전역 변수를 사용하지 않는 경우 
'''
a1 = 1        # 전역 변수 선언
def test(a2) :
    a2 = a2 + 1  # 변수를 변경할 수식
    return a2 # 수식 적용한 변수를 return 값으로 반환
print("전역 변수 a1을 함수 return 값으로 초기화하기 전 : {}".format(a1))
a1 = test(a1)   # a1 = 2 :  함수(return 값)를 이용해 초기화
print("전역 변수 a1을 함수 return 값으로 초기화하기 후 : {}".format(a1))
'''



# 연습 문제
# 1. 사용자가 +,-,*,/ 중 하나를 입력한 후 2개의 정수를 입력해서 연산을 진행하는 프로그램
# 함수 사용해서 작성
'''
def add(a,b) :    # 덧셈 함수 생성
    c = a + b
    return c
def minus(a,b) :  # 뺄셈 함수 생성
    c = a - b
    return c
def mul(a,b) :    # 곱셈 함수 생성
    c = a * b
    return c
def div(a,b) :    # 나눗셈 함수 생성
    c = a / b
    return c
num1 = int(input("첫번째 정수 입력 : "))
num2 = int(input("두번째 정수 입력 : "))
op = input("연산자 입력(+,-,*,/) : ")   # 연산자 선택에 따라 해당 연산 함수 호출
if op == '+' :
    print(add(num1,num2))
elif op == '-' :
    print(minus(num1,num2))
elif op == '*' :
    print(mul(num1,num2))
elif op == '/' :
    print(div(num1,num2))
'''
'''
def cal() :    # 함수 생성
    op = input("연산자 입력(+,-,*,/) : ")
    num1 = int(input("첫번째 정수 입력 : "))
    num2 = int(input("두번째 정수 입력 : "))
    if op == '+' :
        print("두 정수의 덧셈 : {} + {} = {}".format(num1,num2,num1+num2))
    elif op == '-' :
        print("두 정수의 뺄셈 : {} - {} = {}".format(num1,num2,num1-num2))
    elif op == '*' :
        print("두 정수의 곱셈 : {} * {} = {}".format(num1,num2,num1*num2))
    elif op == '/' :
        print("두 정수의 나눗셈 : {} / {} = {}".format(num1,num2,num1/num2))
cal()    # 함수 호출
'''    
'''
def userinput() :
    opq = input("연산자 입력(+,-,*,/) : ")
    n1 = int(input("첫번째 정수 입력 : "))
    n2 = int(input("두번째 정수 입력 : "))
    return opq,n1,n2
def cal() :
    op, num1, num2 = userinput()
    if op == '+' :
        print("두 정수의 덧셈 : {} + {} = {}".format(num1,num2,num1+num2))
    elif op == '-' :
        print("두 정수의 뺄셈 : {} - {} = {}".format(num1,num2,num1-num2))
    elif op == '*' :
        print("두 정수의 곱셈 : {} * {} = {}".format(num1,num2,num1*num2))
    elif op == '/' :
        print("두 정수의 나눗셈 : {} / {} = {}".format(num1,num2,num1/num2))
cal()    
'''

# 2. 사용자가 ipconfig를 입력하면 실제 윈도우에 ipconfig처럼 결과물이 나올 수 있도록 작성
# dir, cls, ping 8.8.8.8 명령어도 사용할 수 있도록 작성
'''
import os
def ipconfig() :
    a = os.system('ipconfig')
    return a
def dir() :
    a = os.system('dir')
    return a
def cls() :
    a = os.system('cls')
    return a
def ping() :
    a = os.system('ping')
    return a
'''
'''
import os 
def cmd(a) :
    if a == 'dir' :
        os.system('dir')
    elif a == 'cls' :
        os.system('cls')
    elif a == 'ipconfig' :
        os.system('ipconfig')
    elif a == 'ping 8.8.8.8' :
        os.system('ping 8.8.8.8')
userin = input("명령어를 입력하세요 : ")
cmd(userin)
'''

# 3. 사용자가 입력한 정수가 홀수인지 짝수인지 판별하는 함수
'''
def evenodd(a) :
    if a%2 == 0 :
        print("입력한 정수 {}는 짝수입니다".format(a))
    else :
        print("입력한 정수 {}는 홀수입니다".format(a))
user = int(input("정수 입력 : "))
evenodd(user)
'''

# 4. 인수값의 총합을 구해서 평균을 반환해주는 함수  ****************************************************************
'''
def avgfunc(*args) :
    sum = 0
    for i in args :
        sum += i
    avg = sum / len(args)
    return avg
num = input("숫자 입력 : ").split()
'''
# num = int(input('정수를 입력하세요 : ').split())      # 에러 --> split은 문자열에서만 사용 가능  *******************
'''
def avg(a) :
    b = []               # 빈 리스트 따로 추가 생성
    for x in a :     
        b.append(int(x))     # 빈 리스트에 (입력)매개변수 값 '정수형'으로 추가(저장)
    sum = 0   
    for i in b :
        sum += i
    return sum / len(b)
num = input('정수를 입력하세요 : ').split()  # split 함수는 문자열에서만 사용, 문자열 리스트로 저장
print('입력한 수의 평균 : {}'.format(avg(num)))
'''




# 재귀 호출(재귀 함수)
# 함수 안에서 똑같은 함수를 호출하는 방식을 의미합니다
# 알고리즘이나 공식을 확인할 때 가독성을 위해 많이 사용합니다 
# 실제 일반인이 사용하는 프로그램에서는 많이 사용하지 않습니다

# 아래와 같이 자기 자신 안에서 자신을 호출하는 문구가 있는 경우를 재귀 호출이라 합니다
# 재귀 호출을 하면 무한 루프처럼 보이지만 일정 시간이 지나면 스택오버플로우(스택 넘침 현상)가 발생하면서 프로그램이 종료됩니다
'''
def test() :
    print("hello")
    test()       # 재귀 호출 : 함수 안에서 자신의 함수를 호출
test()
'''

# 연습 문제
# 1. 1개 이상의 정수를 인수로 받아서 가장 큰 값 그리고 가장 작은 값을 반환하는 pymax(), pymin() 함수를 만들어주세요
'''v1)
def pymax(args) :
    b = []            
    for x in args :     
        b.append(int(x))  
    mx = b[0]
    for i in range(1,len(b)) :
        if b[0] < b[i] :
            mx = b[i]
            i += 1
    return mx
def pymin(args) :
    b = []              
    for x in args :     
        b.append(int(x))   
    mn = b[0]
    for i in range(1,len(b)) :
        if b[0] > b[i] :
            mn = b[i]
            i += 1
    return mn
num = input('정수를 입력하세요 : ').split()
print("입력한 정수 중 가장 큰 값 : {}, 가장 작은 값 : {}".format(pymax(num),pymin(num)))
'''
'''v2)
def pymax(ma) :
    maxlst = []
    for i in ma :
        maxlst.append(int(i))
    return max(maxlst)
def pymin(mi) :
    minlst = []
    for i in mi :
        minlst.append(int(i))
    return min(minlst)

usernum = input('정수 입력 : ').split()
print(f'입력 한 정수 : {usernum}\n가장 큰 수 : {pymax(usernum)}, 가장 작은 수 : {pymin(usernum)}')
'''



# 2. 0 ~ x 까지 또는 x ~ y 까지의 임의 값을 반환하는 함수를 만들어주세요 
# x, y는 사용자가 직접 입력합니다    
'''
from random import *
def rand(a,b) :
    val1 = randint(0,a)
    val2 = randint(a,b)
    return val1,val2
xi = int(input('x값 입력 : '))
yi = int(input('y값 입력 : '))
print("0 ~ {} 또는 {} ~ {} 범위 내 임의의 값 : {}".format(xi,xi,yi,rand(xi,yi)))
'''

















































































































































