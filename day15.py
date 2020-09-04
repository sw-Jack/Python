print()
# 문자열 for 문
'''
for a in "hello" :
    print(a) 
'''

# 연습문제 
# 1. 사용자에게 문자열을 입력 받아서 그 문자열에 공백을 제외한 문자의 개수를 출력하는 프로그램
'''
cnt = 0      # 공백이 아닌 문자의 개수
userin = input("\n문자열 입력 : ")
for a in userin :
    if a == ' ' :    # 입력 받은 문자열이 공백이면 원 조건문으로 continue
        continue
    else : 
        cnt += 1        # 공백이 아닐 경우에 문자 개수 1씩 증가
print("문자열 '{}' 에서 공백을 제외한 문자의 개수 : {}".format(userin,cnt))
'''

'''(더 간단한 코드)
cnt = 0     # 공백이 아닌 문자의 개수
ch = input("\n문자열 입력 : ")
for a in ch :
    if a != ' ' :     # 입력 받은 문자열이 공백이 아니면 
        cnt += 1      # 문자 개수 1씩 증가
print("문자열 '{}' 에서 공백을 제외한 문자의 개수 : {}".format(ch,cnt))
'''


# 2. a ~ z 까지 임의의 문자열을 8자리씩 총 10줄 생성하는 프로그램
'''
from random import *
for a in range(1, 11) :    # 총 10줄 생성
    for b in range(1,9) :     # 8자리 생성
        rand = chr(randint(97,122))  # 다른 표현 : rand = randint(97,122)
        print(rand,end=' ')          #            print("%c" %rand, end = ' ') # 출력문에서 문자형으로 형변환
    print()    # 8자리 돌고 나오면 한 줄 개행                                      
'''


# 3. a ~ z, A ~ z, 0 ~ 9 까지 임의의 문자열을 16자리씩 총 10줄 생성하는 프로그램
'''
from random import *
# 총 10줄 생성
for a in range(1, 11) :
    # 16자리 생성
    for b in range(1,17) :
        # 영소문자, 영대문자, 숫자가 나오는 것도 랜덤이므로
        # 1 나오면 영대문자, 2 나오면 영소문자, 3 나오면 숫자가 나오도록 1 ~ 3 랜덤값 생성
        rand = randint(1,3)
        # 1 이면
        if rand == 1 :     
            # 영대문자 랜덤값 출력, 개행하지 않고 옆으로 이어지도록 계속 출력
            r1 = chr(randint(65,90))
            print(r1,end=' ')
        # 2 이면
        elif rand == 2 :
            # 영대문자 랜덤값 출력, 개행하지 않고 옆으로 이어지도록 계속 출력
            r2 = chr(randint(97,122))       
            print(r2,end=' ')
        # 그 외 경우, 즉 3 이면
        else :      
            # 0 ~ 9 랜덤값 출력, 개행하지 않고 옆으로 이어지도록 계속 출력              
            r3 = randint(0,9)
            print(r3,end=' ')
    # 16자리 모두 돌고 나오면 한 줄 개행
    print()
'''



# 딕셔너리 자료형
# 딕셔너리는 사전이라는 의미를 가지고 있습니다
# 딕셔너리는 반드시 key 와 value 가 한 쌍으로 존재합니다
# 딕셔너리는 순차적을 해당 요소값을 구하지 않고 오로지 key 를 통해 value 를 찾습니다
# 딕셔너리는 인덱스 번호를 사용하지 않습니다
# key 와 value 는 서로 대응 관계에 있습니다
# 딕셔너리는 {} 를 사용합니다

# 사용 형식
'''
a = {key1 : value1, key2 : value2, key3 : value3, ...}
'''
'''
a = {'이름' : '홍길동', '나이' : 20}
print(a)
'''
# 튜플이나 리스트도 딕서녀리 안에 들어올 수 있습니다
'''
a = {"list" : [1,2,3], "tuple" : (1,2,3)}
print(a)
'''
# 딕셔너리 사용 방법
# 기본적으로 딕셔너리의 key 를 통해서 value 를 찾습니다
# 사용 형태
# 딕셔너리 변수명[key] = value
'''
a = {'이름' : '원빈', '나이' : 40}
print(a['이름'])
print(a['나이'])
'''

# 사전에 정수가 들어와 있을 경우 key 와 인덱스 헷갈리지 않도록 주의 
'''
b = {1 : 10, 2 : 20, 3 : 30}
print(b[1]);print(b[2]);print(b[3]) # 대괄호 안 값은 인덱스가 아닌 key!
'''
# 딕셔너리 값 추가
# 사용 형식
# 딕셔너리 변수명[추가하고 싶은 key] = key의 value
'''
dic = {'경력' : '5년'}
dic['희망 연봉'] = '5000만'   # '희망 연봉'이라는 key 와 value 인 '5000만'을 추가
print(dic)
'''
# 딕셔너리 값 삭제
# 사용 형식
# del 딕셔너리 변수명[key]
'''
dict = {1 : 10, 2 : 20, 3 : 30}
del dict[1]   # 대괄호 안에는 key (인덱스 X), key 가 1인 값 삭제
print(dict)
del dict[3]   # 대괄호 안에는 key (인덱스 X), key 가 3인 값 삭제
print(dict)
'''
# 딕셔너리는 중복된 키를 사용할 수 없습니다
# 중복된 키를 입력하면 기존에 있던 키는 삭제가 되고 새로 추가된 키가 생성됩니다
'''
dict = {'이름' : '유재석'}
dict['이름'] = '신동엽'   # '이름'이라는 기존 딕셔너리에 존재하는 중복 key 값 생성
print(dict)
'''
# value 값은 중복이 가능합니다
'''
a = {1 : 10, 2 : 20}
a[3] = 20   # 기존 딕셔너리에 있는 value 값과 중복되는 value 생성
print(a)
'''
# 예시 
'''
나이 = {'홍길동' : 20, '철수' : 25, '영희' : 30}
print(나이)
'''

# 딕셔너리에서 사용할 수 있는 함수
# 1. get 함수
# get 함수는 key로 value 를 가져오는 기능을 가지고 있습니다
# get 함수는 없는 key를 찾을 때 None 이라는 값을 반환합니다(에러 X)
# a[key] 형태와 차이점은 없는 key를 찾을 때 에러의 유무입니다
'''
a = {1 : 10, 2 : 20}
print(a.get(1))         # get 함수
print(a[1])             # a[key] 형태 : 둘다 출력 결과는 동일
'''
# get 함수를 이용해서 value를 구하는 것과 a[key] 형태의 차이  
# 존재하지 않는 key를 입력했을 때 get은 에러 X, None 반환 / a[key] 형태는 에러
'''
a = {1 : 10, 2 : 20}
print(a.get(3))
print(a[3])
'''

# 2. keys 함수
# keys 함수는 딕셔너리 안에 key값만 모아서 객체 형태(dict_keys)로 반환 해주는 함수입니다
# 리스트 형태로만 보고 싶으면 keys() 함수 앞에 list 함수를 사용합니다
# 튜플 형태로만 보고 싶으면 keys() 함수 앞에 tuple 함수를 사용합니다
'''
a = {1 : 10, 2 : 20, 3 : 30}
b = {'이름' : '강호동', '나이' : 50, '직업' : '연예인'}
print(a.keys())      # 객체 형태로 반환
print(b.keys())      # 객체 형태로 반환
print(list(a.keys()))   # 리스트 형태로 반환
print(tuple(b.keys()))  # 튜플 형태로 반환
'''
# for 문에서 활용 가능
'''
a = {1 : 10, 2 : 20, 3 : 30}
b = {'에피타이저' : '스프', '메인 메뉴' : '파스타', '디저트' : '커피'}
for key1 in a.keys() :
    print(key1, end = ' ')
print()
for key2 in b.keys() :
    print(key2, end = ' ')
print()
'''































        
