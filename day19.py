print()
# 연습 문제
# 1. 1개 이상의 정수를 인수로 받아서 가장 큰 값 그리고 가장 작은 값을 반환하는 pymax(), pymin() 함수를 만들어주세요
'''
def pymax(args) :
    b = []                # 빈 리스트 생성
    for x in args :     
        b.append(int(x))    # 빈 리스트에 문자열형을 정수형으로 강제 형변환하면서 추가
    mx = b[0]       # 리스트의 첫번째 값을 최대값으로 초기화
    for i in range(1,len(b)) :  # 리스트의 첫번째 값을 나머지 값들과 하나씩 비교
        if mx < b[i] :
            mx = b[i]           # 최대값보다 큰 값이 나타나면 그 값을 최대값으로 설정
    return mx                  # 최대값 반환
def pymin(args) :
    b = []                # 빈 리스트 생성
    for x in args :     
        b.append(int(x))    # 빈 리스트에 문자열형을 정수형으로 강제 형변환하면서 추가
    mn = b[0]       # 리스트의 첫번째 값을 최소값으로 초기화
    for i in range(1,len(b)) :  # 리스트의 첫번째 값을 나머지 값들과 하나씩 비교
        if mn > b[i] :
            mn = b[i]          # 최소값보다 작은 값이 나타나면 그 값을 최소값으로 설정
    return mn                 # 최소값 반환
num = input('정수를 입력하세요 : ').split()     # split() 함수를 통해 한번에 정수 입력받기 -> 입력한 정수는 문자열 리스트형으로 저장
print("입력한 정수 중 가장 큰 값 : {}, 가장 작은 값 : {}".format(pymax(num),pymin(num)))
'''

'''(튜플 이용)
def pymax(*args) :         # 매개변수 앞에 *을 붙이면 인수들이 매개변수에 튜플 형태로 저장
    mx = args[0]           # 최대값을 입력받은 (튜플의) 첫 값으로 초기화
    for i in args[1:] :    # 변수 i에 튜플 형태의 매개변수 값들을 넣고 원소 하나씩 비교
        if i > mx :
            mx = i         # 최대값보다 큰 수가 나타나면 그 수를 최대값으로 설정
    return mx              # 최대값 반환
def pymin(*args) :         # 매개변수 앞에 *을 붙이면 인수들이 매개변수에 튜플 형태로 저장
    mn = args[0]           # 최소값을 입력받은 (튜플의) 첫 값으로 초기화
    for i in args[1:] :    # 변수 i에 튜플 형태의 매개변수 값들을 넣고 원소 하나씩 비교
        if i < mn :
            mn = i         # 최소값보다 작은 수가 나타나면 그 수를 최소값으로 설정
    return mn              # 최소값 반환
print("최대값 : ",pymax(1,2,3,4,5))
print("최소값 : ",pymin(1,2,3,4,5))
'''


# 2. 0 ~ x 까지 또는 x ~ y 까지의 임의 값을 반환하는 함수를 만들어주세요 
# x, y는 사용자가 직접 입력합니다    
'''
from random import *
def rand(a,b) :
    val1 = randint(0,a)
    val2 = randint(a,b)
    return val1,val2      # 각 범위에 해당하는 랜덤값 2개 한꺼번에 반환 -> 튜플 형태 반환
xi = int(input('x값 입력 : '))
yi = int(input('y값 입력 : '))
print("0 ~ {} 또는 {} ~ {} 범위 내 임의의 값 : {}".format(xi,xi,yi,rand(xi,yi)))
'''

'''
from random import *
def ran(min,max=0) :   # 인수가 들어올 때 앞 매개변수 부터 저장 (한개들어오면 min은 입력값 max는 디폴트값 0)
    if max == 0 :     # 두번째 인수가 입력되지 않아 함수의 매개변수 값이 디폴트 값 0으로 유지되면,
        min,max = max,min   # 매개변수 max와 min 스위치 (서로 값 바꾸기)
    a = randint(min,max)
    return a
x = int(input('x값 입력 : '))
y = int(input('y값 입력 : '))
print("{} ~ {} : {}".format(x,y,ran(x,y)))
print("0 ~ {} : {}".format(x,ran(x)))
'''



# 재귀 호출(재귀 함수)
# 함수 안에서 똑같은 함수를 호출하는 방식을 의미합니다
# 알고리즘이나 공식을 확인하 때 가독성을 위해 많이 사용합니다 
# 실제 일반인이 사용하는 프로그램에서는 많이 사용하지 않습니다

# 아래와 같이 자기 자신 안에서 자신을 호출하는 문구가 있는 경우를 재귀 호출이라 합니다
# 재귀 호출을 하면 무한 루프처럼 보이지만 일정 시간이 지나면 스택오버플로우(스택 넘침 현상)가 발생하면서 프로그램이 종료됩니다
'''
def test() :
    print("hello")
    test()
test()
'''



# 피보나치 수열 1,1,2,3,5,8,13,21,34,55...
# 피보나치는 n이 0일 때, 0을 return하고 1이면 1을 return 합니다 
# 2이상이면 이전의 두 값을 더합니다
'''
def fib(n) :
    if n == 0 :
        return 0
    elif n == 1 :
        return 1
    return fib(n-2) + fib(n-1)
for i in range(0,20) :
    print(fib(i), end = ' ')
'''

# 모듈 (module)
# 함수나 클래스를 하나의 파일에 모아 놓은 파일을 의미합니다
# 모듈을 생성하면 다른 파이썬 파일에서도 모듈을 불러와서 
# 그 모듈에 정의되어 있는 함수나 클래스를 사용하는 것이 가능합니다
# 모듈의 장점은 파이썬 파일마다 동일한 함수를 만들지 않아도 되며 
# 다른 사람이 만들어 놓은 모듈을 사용할 수 있기 때문에 호환성이 뛰어납니다
# 사용 형식
# from random import random

# import 만 사용하는 경우
# 사용 형식
# import 모듈이름
# import만 쓴다면 함수를 사용할 때 반드시 모듈이름.함수명() 방식으로 사용해야합니다
'''
import mod
import os
print(mod.add(1,2))
os.system('ping 8.8.8.8')
'''

# from과 import를 사용하는 경우
# 사용 형식
# from 모듈이름 import 모듈함수
# from을 사용하면 모듈을 사용할 때 모듈의 이름을 적지 않고 함수만으로 바로 사용할 수 있습니다
'''
from mod import add
from os import system
print(add(1,2))
system('ping 8.8.8.8')
'''

# 모듈의 사용 위치
# 모듈은 만든다고 바로 마음대로 사용할 수 없습니다
# 모듈을 사용하려면 자신이 지금 사용하고 있는 파이썬 파일이 들어있는 폴더에 모듈이 존재해야합니다
# 아니면 파이썬 설치 폴더(환경 변수) 안에 들어있는 경우 사용할 수 있습니다


# 연습 문제 : 컴퓨터와 가위바위보 게임
# 5판 3선승으로 진행합니다
# 한 판 진행할 때마다 결과가 출력이 되어야 합니다
# 가위바위보가 끝나면 승,패,무 결과가 출력되면서 계속 할 것인지 물어봐야 합니다
# 출력 양식 -> 승 : 1, 패 : 1, 무 : 1
'''
from random import *
while True :
    win, draw, lose = 0, 0, 0
    while True :
        user = input("\n<가위바위보 게임>\n가위 바위 보 중 선택하세요 : ")
        com = randint(1,3)
        if com == 1 :
            com = '가위'
            print("*컴퓨터 : {}".format(com))
        elif com == 2 :
            com = '바위'
            print("*컴퓨터 : {}".format(com))
        else :
            com = '보'
            print("*컴퓨터 : {}".format(com))
        if user == com :
            draw += 1
            print('*결과 : 무')
        elif user == '가위' :
            if com == '보' :
                win += 1
                print('*결과 : 승')
            else :
                lose += 1
                print('*결과 : 패')      
        elif user == '바위' :
            if com == '가위' :
                win += 1
                print('*결과 : 승')
            else :
                lose += 1
                print('*결과 : 패')
        elif user == '보' :
            if com == '바위' :
                win += 1
                print('*결과 : 승')
            else :
                lose += 1
                print('*결과 : 패')
        else : 
            print("다시 입력하세요")
            continue
        if win == 3 :
            print("\n<결과>\n승리!\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            break
        elif win+draw+lose == 5 :
            if win > lose :
                print("\n<결과>\n승리!\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))       
            elif win == lose : 
                print("\n<결과>\n무승부!\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            else :
                print("\n<결과>\n패!\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            break
    q = input("한판 더 하시겠습니까 (y/n) : ")
    if q == 'y' :
        continue
    else : 
        break
'''


 
     
    










































