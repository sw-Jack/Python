print()
# 튜플
# 역할은 리스트와 동일하나 리스트와 차이점이 존재합니다
# 튜플은 ()을 사용합니다
# 튜플은 요소값을 변경할 수 없습니다
'''
a = ()  # 빈 튜플

b = (1,2,3)  # 튜플의 일반적인 형태
print(b)

c = 1,2,3   # 괄호를 사용하지 않아도 튜플로 인식할 수 있음
print(c)

d1 = (1,)  # 튜플의 요소값이 하나인 경우에는 뒤에 ,(쉼표)를 붙여줘야 함(붙여주지 않은 경우 숫자는 정수형)
print(d1)  
d2 = (1)    # 쉼표가 없어 일반 정수형 1로 인식
print(d2)

e = (1,'안녕하세요',(2,3)) # 튜플안의 튜플도 가능
print(e)
'''

# 튜플 사용법
'''
a = (1,2,3)
print(a[1])  # 튜플도 리스트와 동일하게 인덱싱 사용 가능
print(a[0:2])  # 슬라이싱도 사용 가능
print(a[0]+a[1]+a[2])  # 요소값 간 사칙 연산
print(a[-1])  # 음수 인덱싱
'''

# 튜플의 요소값 수정
# 튜플은 요소값 수정이 불가능합니다
'''
a = 1,2,3
a[0] = 10    # 요소값 변경 불가능  # 오류
print(a)
'''
'''
a = 1,2,3
del a[0]     # 요소값 삭제 불가능  # 오류
print(a)
'''

# 튜플에서 사용 가능한 함수
# 1. len 함수
# 튜플의 길이를 반환해주는 함수
'''
a = ()
b = 1,2,3,4,5
c = ('P','y','t','h','o','n')
print(a);print(b);print(c)
print(len(a),len(b),len(c))
'''


# 2. count 함수
# count 함수는 튜플에서도 사용할 수 있습니다. 효과는 리스트랑 동일
'''
a = 1,2,3,4,1,22,32,4
b = ('h','e','l','l','o','w','o','r','l','d')
c = a.count(4) + b.count('l')
print(a.count(1))
print(b.count('o'))
print("{} + {} = {}".format(a.count(4),b.count('l'),c))
'''

# 3. index 함수
# index 함수도 튜플에서 사용할 수 있습니다. 효과는 리스트랑 동일
'''
a = 1,2,3
b = ("let's","study","python")
c = a + b
print(a);print(b);print(c)
print(a.index(3))
print(b.index("python"))
print(c.index("let's"))
'''

# 4. tuple 함수
# 리스트나 문자열 등을 튜플 형태로 변환시키는 기능을 가지고 있는 함수입니다
'''
a = [1,2,3]    # 리스트 -> 튜플
b = '안녕하세요'   # 문자열 -> 튜플
print(tuple(a))
print(tuple(b))
print(tuple('hello python!'))  # 문자열 -> 튜플
'''

# 5. list 함수
# 튜플이나 문자열 등을 리스트 형태로 변환시키는 기능을 가지고 있는 함수입니다
'''
a = (55,2,3,10,100)
b = 'j','a','c','k'
c = "LET'S GO!"
print(list(a))    # 튜플 -> 리스트
print(list(b))    # 튜플 -> 리스트
print(list(c))    # 문자열 -> 리스트
print(list('hello'))    # 문자열 -> 리스트
'''

# 6. max, min 함수
# max는 요소값 중에서 가장 큰 값을 반환해주며 min은 가장 작은 값을 반환합니다
'''
a = 1,2,3,4,5
b = 'a','b','c','d','e','f'   # 알파벳 튜플
print(max(a))
print(min(a))
print(max(b))  # 알파벳 문자의 튜플의 값의 크기는 알파벳 순서 뒤로 갈수록 큰 값
print(min(b))  # 알파벳 문자의 튜플의 값의 크기는 알파벳 순서 앞일수록 작은 값
'''

# 리스트에서도 사용 가능
'''
a = [1,2,3]
print(max(a))
print(min(a))
'''

# for 반복문
# while 문과 마찬가지로 종속 문장을 반복하는 기능을 가지고 있습니다
# while과는 다르게 조건식을 사용하지 않습니다
# for 문을 사용하면 코드가 간단하게 표현된다는 장점이 있습니다

# 사용 형식
'''
for 변수 in 튜플/리스트/문자열/range() :
    종속문장1(수행코드1)
    종속문장2(수행코드2)
'''

# 실제 사용 형식
# 가장 먼저 리스트의 첫번째 요소값 (인덱스0)을 a 변수에 초기화 시킵니다
# 그리고 for 문의 종속 문장을 실행하고 종속 문장을 모두 실행하면
# 이번에는 2번째 요소값(인덱스1)을 a 변수에 초기화 시킵니다
# 위 과정을 리스트의 요소값을 다 초기화할 때 까지 반복합니다
# 더 이상 초기화할 요소값이 없으면 반복문을 종료합니다
'''
for a in [1,2,3] :   # 리스트
    print(a)
print('-'*5)
for a in (1,2,3) :   # 튜플도 결과 동일
    print(a)
print('-'*5)
for a in '123' :     # 문자열도 결과 동일
        print(a)
'''

# range() 함수
# range 함수는 정수의 범위를 지정해서 반환하는 기능을 가지고 있는 함수입니다
# range (x,y) 형태로 많이 사용합니다
# x가 범위의 시작 y가 끝을 의미하지만 y는 자기 자신을 포함하지 않습니다
# 즉 x이상 y미만의 범위를 반환합니다
'''
print(range(0,10))          # 0 ~ 9
print(range(1,101))         # 1 ~ 100
print(tuple(range(0,10)))   # 0 ~ 9 튜플
print(list(range(0,10)))    # 0 ~ 9 리스트
'''


# range 함수는 range(x,y,z) 형태로도 사용 가능합니다
# x는 시작 y는 끝을 나타내지만 z는 증감을 나타냅니다
'''
print(list(range(0,10,2)))  # 0 ~ 9 까지, 0에서 시작해서 2씩 증가
print(list(range(10,0,-1))) # 10 ~ 1 까지, 10에서 시작해서 -1씩 감소
print(list(range(10,0,-2))) # 10 ~ 1 까지, 10에서 시작해서 -2씩 감소
'''
'''
for a in range(0,10) : 
    print(a,end=' ',)
print()
for b in range(1,10,2) :
    print(b,end=' ')
'''


# 연습 문제
# 1. grade = [70,60,55,75,95,90,80,80,85,100] 를 합해서 평균을 구하는 프로그램(for문)
'''
grade = [70,60,55,75,95,90,80,80,85,100]
sum = 0
for a in grade :
    sum += a          # grade 리스트의 요소값을 변수 a에 하나씩 저장하며 누적합
avg = sum / len(grade)   # len 함수 이용 평균 구하기
print("합 : {}, 평균 : {}".format(sum,avg))
'''

# 2. 1 ~ 50 까지의 값을 for를 사용해서 출력하지만 7의 배수는 출력하지 않습니다
'''
cnt = 0
for a in range(1,51) :
    if a%7 == 0 :
        continue
    else :
        cnt += 1
        if cnt%5 == 0 :
                print(a)
        else :
                print(a,end='\t')
'''
'''
for a in range(1,51) :
        if a%7 != 0 :
                print(a,end=' ')
        continue
'''
# 3. 1 ~ 30 까지의 값을 반복문을 사용하여 출력할 때 다음과 같은 형식으로 출력되도록 합니다
'''
1  2  3  4  5
....
26 27 28 29 30
'''
'''
cnt = 0                    # 숫자 카운트 변수 생성
for a in range(1,31) :
    cnt += 1               # 값 입력될 때 마다 카운트 1씩 증가
    if cnt%5 == 0 :        # 카운트 값이 5의 배수이면 한 줄 개행 출력
        print(a) 
    else :                 # 이외 값은 그 줄에 간격 맞춰 출력
        print(a,end='\t')
'''
'''(case2)
for a in range(1,31) :
    if a%5 == 0 :       # 숫자가 5의 배수이면 한줄 개행하여 출력
        print(a)
    else :              # 숫자가 5의 배수가 아니면 간격 맞춰 한줄에 출력
        print(a,end='\t')
'''

# 4. 구구단 전체 출력
'''
for a in range(1,10) :
    print("\n<{}단>".format(a))
    for b in range(1,10) :
        print("{} X {} = {}".format(a,b,a*b))
'''

# for 문 continue
# while continue 와 동일
'''
for i in [1,2,3] :
    if i == 2 :
        continue  # continue 아래의 문장은 실행 X, 2는 출력 X
        print(i)
    print(i)
'''

# for 문 break
'''
for i in [1,2,3] :
    print(i) 
    break  # 변수 i에 1 값이 들어간 첫번째 반복문에서 i 값 출력 바로 종료
'''














































































































































