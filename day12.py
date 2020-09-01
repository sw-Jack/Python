print()
# 문자열 함수
# 11. lstrip 함수 
# lstrip 는 맨 왼쪽에 있는 공백을 삭제하는 함수입니다
'''
a = " hello"
b = "    Hello World"
print(a);print(b)
a = a.lstrip()
b = b.lstrip()
print(a);print(b)
'''

# 12. strip 함수
# strip 함수는 양쪽 공백을 지우는 함수입니다
'''
a = ' hello '
b = ' Hello World '
print("양 쪽 공백 삭제 전 : {}".format(len(a)))
print("양 쪽 공백 삭제 전 : {}".format(len(b)))
a = a.strip()
b = b.strip()
print("양 쪽 공백 삭제 후 : {}".format(len(a)))
print("양 쪽 공백 삭제 후 : {}".format(len(b)))
'''


# 13.split 함수
# split 함수는 문자열을 나눌 때 사용하는 함수입니다
# split() 안에 아무것도 적지 않으면 공백을 기준으로 문자열을 나눕니다
# split은 문자열을 나누고 리스트 형식으로 저장합니다
'''
a = 'Hello my name is Lee'
print(a.split())
'''
'''
a = "apple,banana,peach,mango,cherry"
print(a.split(','))
'''


# 리스트 (list)
# 리스트는 여러 종류의 값을 하나로 묶어서 변수에 초기화해서 사용하는 문법
# 리스트는 []를 사용합니다
# 요소값은 ,로 구분을 해줘야합니다
# 리스트 생성 방법
''''
a = [1,2,3]    # 정수형
b = ['1','2','3']    # 문자형
c = ['hello','안녕']    # 문자열형
d = [0.3,5.0,7.7,109.5]    # 실수형
e = [1,'Python','3',4.5,'여름',10]    # 혼합형
f = []    # 빈 리스트 생성 (후에 값 삽입 가능)
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
'''


# 리스트의 인덱싱
# 리스트도 문자열과 마찬가지로 인덱스 번호를 사용해서 요소값을 사용할 수 있습니다
'''
a = [1,2,3]
b = ['안','녕','하','세','요']
print(a[0],a[1],a[2])
print(a[-1],a[-2],a[-3])
print(a[0]+a[-1])     
print(b[0],b[-1])     
print(b[0]+b[1]+b[2]+b[3]+b[4]) 
'''


# 리스트의 슬라이싱
'''
a = [1,20,30,400,5]
print(a[0:2])
print(a[-3:-1])
print(a[:5])
print(a[2:])
print(a[:])
'''

# 리스트의 요소값 변경
'''
a = [1,2,3]
a[0] = 100   
a[2] = 4        # 인덱스 번호를 이용해서 요소값 변경이 가능합니다
print(a)
'''
'''
a = [1,2,3]
a[0] = 'hello'    
a[1] = 3.14            # 문자열로 변경하는 것도 가능합니다
print(a)
'''
'''
a = [1,2,3,4,5]
a[0] = a[1]*10
a[1] = a[0]+4
a[4] = a[2]*a[3]
print(a)
'''


# 슬라이싱을 이용한 리스트 요소값 변경
'''
a = [1,2,3]
b = [4,5,6,7,8]
a[0:2] = [4,5]       # 인덱스 번호 0 ~ 1번에 해당하는 요소값을 각각 4와 5로 초기화
b[:5] = ['안','녕','하','세','요']     # 문자열도 정상적으로 변경 가능
print(a)
print(b)
'''

# 연습 문제
# 분식집에서 라면, 만두, 떡볶이 3가지를 팔고 있습니다
# 가격은 라면 2000원, 만두 500원, 떡볶이 1000원입니다
# 음식의 가격을 사용자가 입력한 가격으로 바꿀 수 있는 프로그램 만들기
# 조건
# 반드시 리스트를 사용합니다
# 가격은 사용자가 직접 입력할 수 있도록 만들어 줍니다
# 프로그램은 다음과 같은 기능을 가지고 있어야 합니다
# 1. 메뉴 확인
# 2. 가격 확인
# 3. 가격 변경
# 4. 메뉴 변경
# 5. 프로그램 종료
'''
menu = ['라면','만두','떡볶이']
price = [2000,500,1000]
while True :
    idx = 0
    userin = int(input("\n1.메뉴 확인\n2.가격 확인\n3.메뉴 변경\n4.가격 변경\n5.프로그램 종료\n번호를 선택하세요 : "))
    if userin == 1 :
        print("<메뉴 확인>\n{}".format(menu))
    elif userin == 2 :
        print("<가격 확인>\n{}".format(price))
    elif userin == 3 :
        exm = input("\n<메뉴 변경>\n변경할 메뉴를 선택하세요 : ")
        m = input("변경할 이름 입력 :")
        while idx < 3 :
            if exm == menu[idx] :
                menu[idx] = m
            idx += 1
        print("변경 메뉴 : {}".format(menu))       
    elif userin == 4 :
        exp = input("\n<가격 변경>\n변경할 가격의 메뉴를 선택하세요 : ")
        p = int(input("변경할 가격 입력 : "))
        while idx < 3 :
            if exp == menu[idx] :
                price[idx] = p
            idx += 1          
        print("변경 가격 : {}".format(price))
    elif userin == 5 :
        print("프로그램 종료")
        break
'''

'''
menu = ['라면','만두','떡볶이']
price = [2000,500,1000]
while True :
    idx = 0
    userin = int(input("\n1.메뉴 확인\n2.가격 확인\n3.가격 변경\n4.메뉴 변경\n5.프로그램 종료\n번호를 선택하세요 : "))
    if userin == 1 :
        print("<메뉴 확인>\n{}".format(menu))
    elif userin == 2 :
        print("<가격 확인>\n{}".format(price))
    elif userin == 3 :
        exp = input("\n<가격 변경>\n변경할 가격의 메뉴를 선택하세요 : ")
        p = int(input("변경할 가격 입력 : "))
        if exp == menu[0] :
            price[0] = p
        elif exp == menu[1] :
            price[1] = p
        elif exp == menu[2] :
            price[2] = p    
        print("변경 가격 : {}".format(price))        
    elif userin == 4 :
        exm = input("\n<메뉴 변경>\n변경할 메뉴를 선택하세요 : ")
        m = input("변경할 이름 입력 :")
        if exm == menu[0] :
            menu[0] = m
        if exm == menu[1] :
            menu[1] = m
        if exm == menu[2] :
            menu[2] = m
        print("변경 메뉴 : {}".format(menu))
    elif userin == 5 :
        print("프로그램 종료")
        break
'''



# 이중 리스트
# 이중 리스트는 리스트 안에 리스트가 하나 더 존재하는 것을 의미합니다
# 사용 형식
'''
a = [1,2,3,[4,5,6]]
print(a[3])

print(a[3][0])     # a라는 리스트의 인덱스 번호 3번에 해당하는 리스트의 인덱스 번호 0번을 출력
print(a[3][1])     # a라는 리스트의 인덱스 번호 3번에 해당하는 리스트의 인덱스 번호 1번을 출력
print(a[3][2])     # a라는 리스트의 인덱스 번호 3번에 해당하는 리스트의 인덱스 번호 2번을 출력

print(a[3][:2])    # 슬라이싱도 사용 가능
'''

# 삼중 리스트
'''
a = [1,2,[3,4,[5,6]]]
print(a[2][2][0]) # a라는 리스트의 인덱스 2번에 해당하는 리스트의 인덱스 2번에 해당하는 인덱스 0번 출력
print(a[2][2][1]) # a라는 리스트의 인덱스 2번에 해당하는 리스트의 인덱스 2번에 해당하는 인덱스 1번 출력

print(a[2][1:])   # 이중 리스트 슬라이싱 
print(a[2][2][:]) # 삼중 리스트 슬라이싱
'''


# 리스트 더하기 
# 리스트의 더하기 연산은 2개의 리스트를 서로 합치는 기능을 가지고 있습니다
'''
a = [1,2,3]
b = [4,5,6]
c = ['python','java','jsp','c++']
print(a+b)
print(b+a)
print(a+c)
print(c+b)
'''

# 리스트 곱하기
'''
a = [1,2,3]
b = [4,5,6]
c = ['c','c++','java','jsp']
print(a*3)
print(c*2)
print(a*2+c)
print((a+b)*2)
'''

# 리스트의 요소값 삭제
# del을 사용해서 리스트 안에 요소값을 삭제할 수 있습니다
'''
a = [1,2,3]
print(a)
del a[1]
print(a)
del a[1]
print(a)
'''

# 리스트의 길이 구하기
# len 함수를 사용해서 리스트의 요소값의 개수를 알 수 있습니다
'''
a = [1,2,3]
b = ['python','java','jsp','c','c#']
print(len(a))
print(len(b))
'''


# 리스트에서 사용할 수 있는 함수
# 1. append 함수
# 리스트에 요소값을 추가해주는 함수입니다
# append() 안에 추가하고 싶은 요소값을 입력합니다
# append는 리스트에 맨 뒤에 추가됩니다
'''
a = []
print(a)
a.append(10)
a.append(11)
a.append('Lee')
a.append('파이썬')
print(a)
'''
# 리스트도 추가 가능
'''
a = [1,2,3]
a.append([4,5,6])   
print(a)
a.append(['java','python','c++'])
print(a)
'''




























