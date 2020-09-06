print()
# isdecimal() 함수
# isdecimal 함수를 사용하면 입력한 "문자열이 정수형"으로 변환이 가능한지 안한지 True 와 False 중 하나로 반환합니다 
# 변환이 가능하면 True, 반환이 가능하지 않으면 False
'''
a = '123'
print(a.isdecimal())
b = '안녕하세요'
print(b.isdecimal())
'''
# isdecimal 함수 이용 day16 문제
'''
name = {}
chkey = 1
while 1 :
    print("""1.ID추가
2.ID수정
3.ID확인
4.ID삭제""")
    num = int(input("원하시는 번호를 입력해주세요 : "))
    if num == 1 :
        a = input("추가하고 싶은 ID를 입력하세요 : ")
        name[chkey] = a
        chkey = chkey + 1
        print(name)
    elif num == 2 :
        print(name)
        a = input("ID의 번호나 ID를 입력하세요 : ")
        if a.isdecimal() :
            if int(a) in list(name.keys()) :
                chID = input("바꾸고 싶은 ID를 입력하세요 : ")
                name[int(a)] = chID
                print(name)
            else :
                print("없는 번호입니다 다시 입력하세요")
        elif a in list(name.values()) :
            chid = input("바꾸고 싶은 ID를 입력하세요 :")
            b = list(name.values())
            count = 0
            for c in b :
                count = count+1
                if c == a :
                    name[count] = chid
                    print(name)
        else :
            print("없는 ID입니다 다시 입력하세요")
    elif num == 3 :
        print(name)
    elif num == 4 :
        print("프로그램을 종료 합니다")
        break
'''







# 함수(function)
# 동일한 기능을 가지고 있는 문장들을 하나의 함수로 만들어서 사용할 수 있습니다
# 즉 똑같은 기능을 가지고 있는 코드들을 하나의 함수로 정의해서 사용하면 코드가 훨씬 쉽고 간결하게 표현하는 것이 가능합니다
# 사용 형식
'''
def 함수명(매개변수) :       # def는 함수를 선언할 때 사용하는 예약어
   종속문장1                 # 종속문장은 마찬가지로 들여쓰기를 해야함
   종속문장2 
   return 반환값
'''
'''
def num_mul(a,b) :
    return a*b
print(num_mul(2,5))
'''
'''
def num_add(a,b) :
    c = a+b
    return c
print(num_add(1,2))
'''

# 함수의 사용 형태
# 인수와 매개변수가 없는 형태
'''
def st1() :
    return "안녕하세요"
print(st1())
'''
'''
def st2() :
    print("안녕하세요")
    b = input("이름 : ")
    return b
print(st2())
'''

# return 값이 없는 형태
# return 을 쓰지 않으면 출력 결과는 None 이라고 나옵니다
# return 이 없어서 실제 반환된 값이 없기 때문에 아무것도 출력할 수 없습니다
'''
def add(a,b) :
    c = a + b
print(add(1,2))   # None 반환
'''
'''
def add(a,b) :
    c = a + b
    print(c)      # 함수 안에서 출력
add(1,2)
'''

# return, 매개변수 그리고 인수도 없는 형태
'''
def inp() :
    a = int(input("정수 입력 : "))
    b = int(input("정수 입력 : "))
    print(a+b)
inp()
'''

# 인수가 몇개 들어오는지 알 수 없는 경우
# 매개변수 앞에 *을 붙이면 인수값들을 튜플 형태로 매개변수에 저장합니다 -> 매개변수로 들어오는 불특정 다수의 값을 튜플 형태로 받아서 처리
# 매개변수 이름(args)은 자유롭게 지정 가능합니다
'''
def sum_add(*args) :
    print(args)          # 입력값들이 튜플 형태로 저장되어 있음
    sum = 0
    for i in args :
        sum += i
    return sum
print(sum_add(10,20,30,40,50))
'''
# 문자열로도 구성 가능
'''
def test(*args) :
    print(args)
test('안','녕','하','세','요')
test('안녕하세요','반갑습니다')
'''
# 문자열과 숫자 섞어서 사용 가능
'''
def test(*args) :
    print(args)
test(1,'안녕',5.5)
'''
# 함수는 종속문장에서 return을 만나 값을 반환하면 그 즉시 함수를 종료합니다
# 반복문에서 break와 비슷한 역할을 하고 있습니다
'''
def test(st,*args) :
    print(args)
    if st == '+' :
        sum = 0 
        for i in args :
            sum += i
        return sum
    elif st == '-' :
        sum = 0
        for i in args :
            sum -= i
        return sum
print(test('+',10,20,30))
print(test('-',10,20,30))
'''

'''
def test(st,*args) :
    print(args)
    if st == '+' :
        sum = 0 
        for i in args :
            sum += i
            return sum
    elif st == '-' :
        sum = 0
        for i in args :
            sum -= i
            return sum
print(test('+',10,20,30))
print(test('-',10,20,30))
'''



# 기본적으로 함수 안에서 사용하는 변수는 함수 밖에서 사용할 수 없습니다
# 지역 변수 : 함수 안에서 사용하는 변수
'''
def num_add(a,b) :
    c = a+b    # 변수 c는 함수 내에서 선언된 지역 변수
    return c
print(num_add(1,2))
print(c)      # 에러
'''
'''
def ex(a) :
    a = 1   # 함수 내 지역 변수 선언
    return a
print(a)    # 에러
'''

# 전역 변수 (광역변수)
# 전역 변수 global을 사용하면 더 이상 함수 안에서만 사용하는 것이 아닌 함수 밖에 있는 변수를 사용한다는 뜻입니다
'''
a = 0
def test() :
    a = 0
    a = a + 1
    print(a)
test()
print(a)   # 변수 a의 값은 함수 안의 a 값 관계없이 함수 밖에서 선언된 전역 변수 a값으로 유지
'''
'''
a = 0
b = 0
def test() :
    global a      # 전역 변수 선언 : 함수 밖에 선언되어 있는 전역 변수에 영향을 줌
    a = a + 1
    b = 1         # 지역 변수 선언
test()
print(a)      # global 변수로 a = 0 + 1 적용, 출력
print(b)      # 함수 호출과 상관없이 전역 변수 a의 원래 값 0 출력
'''
'''
a, b = 10, 20   # 전역 변수 a, b 선언
def test() :
    a = 0     
    b = 10       # 지역 변수 a, b 선언 
    print(a,b)
print(a,b)      # 전역 변수 a, b의 값 출력
test()          # 함수 호출시 함수 내에서 선언한 지역 변수 a, b의 값 출력
print(a,b)      # 함수 호출 이후에도 변수 a,b 값은 전역 변수 값을 유지
'''
























































