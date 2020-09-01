print()
# 문자열의 인덱싱과 슬라이싱
# 인덱싱
# 인덱싱(indexing)은 인덱스 번호(0부터 시작)를 사용해서 변수의 특정 문자 하나를 사용하고 싶을 때 사용하는 방법
# 인덱스 번호는 0번부터 시작하며 공백도 인덱스 번호에 포함됩니다
'''
a = "Hello my name is Lee"
print(a[0])  # index 0번 출력
print(a[5])  # index 5번 출력 -> 공백 출력
print(a[6])  # index 6번 출력 
'''
'''
a = "Hello my name is Lee"
print(a[-1])                # 알파벳 o 출력 : -1은 문자열의 맨 뒤에서부터 첫번째 인덱스 번호를 의미합니다
print(a[3*2])               # 인덱스 번호를 연산을 통해서 표현하는 방법도 가능합니다s
'''

# 슬라이싱
# 슬라이싱(Slicing)은 인덱스 번호를 사용해서 특정 문자 하나가 아니라 인덱스 번호의 범위를 지정하여 한번에 자르는 방법
'''
a = "Hello my name is Lee"
print(a[0:4])    # 인덱스 번호 0이상 4미만 즉, 0 ~ 3번 까지의 인덱스 번호 값 한번에 출력
print(a[0:5])    # 인덱스 번호 0이상 5미만 즉, 0 ~ 4번 까지의 인덱스 번호 값 한번에 출력 

print(a[0:])     # 인덱스 번호 0 ~ 끝까지 한번에 출력
print(a[:5])     # 인덱스 번호 처음부터 ~ 4번 까지 한번에 출력
print(a[:])      # 처음부터 ~ 끝까지 한번에 출력

print(a[0:-2])   # 인덱스 번호 0 ~ -3 까지 한번에 출력
'''

# 슬라이싱 사용 예제
'''
a = '안녕하세요 반갑습니다'
b = a[0:5]
c = a[5:]
print(b+c)
print(a[0]+a[1]+a[2]+a[3]+a[4])
'''

# 연습 문제 
# name 이라는 변수에 들어있는 문자열을 사용해서 보기와 같은 문자를 만들어 주세요
'''
name = "velatreicdf"
# <보기>
# ice
print(name[7:9]+name[1])
# fire
print(name[-1]+name[-4]+name[5:7])
# tell
print(name[4]+name[1]+name[2]*2)
# reds
print(name[5:7]+name[-2])
# velvet
print(name[:3]+name[:2]+name[4])
'''

# 문자열은 인덱스 번호를 사용해서 요소값을 수정할 수 없습니다 **
'''
a = 'heiio'
a[2] = 'l'
print(a[2])            # 오류
'''

# 아래 방식을 사용하면 변수의 문자열 변경은 가능합니다 **
# 하지만 a변수를 완전히 초기화 시킨 것이므로 요소값을 수정한 것은 아닙니다
'''
a = 'heiio'
a = a[0:2] + 'l' + 'l' + a[-1]
print(a)
'''

# 문자열에서 사용할 수 있는 함수

# 1. len 함수
# 문자열의 길이를 반환해주는 함수입니다
# 쉽게 말하면, 문자열의 글자수를 의미합니다
'''
a = 'hello'
b = "My name is Lee"
print(len(a))
print(len(b))
'''

'''
pw = 'asd1234'
if len(pw) < 11 :
    print("잘못 입력")
'''

# 숫자는 사용할 수 없습니다
'''
a = 123
b = 1024
print(len(a))    # 오류
print(len(b))    # 오류
'''

# 2. count 함수
# count 함수는 문자의 개수를 반환해주는 함수입니다
# 해당 문자가 존재하지 않으면 0을 반환합니다
'''
a = "Hello Wolrd"
print(a.count('l'))
print(a.count('ll'))
print(a.count('W'))
'''
'''
a = ['abc','def']
print(a.count('abc'))
print(a.count('def'))
print(a.count('bcd'))
'''

# 3. join 함수
# join 함수는 입력한 문자열이 원 문자열 문자 사이사이에 삽입됩니다
'''
a = 'Hello Python'
print('|'.join(a))
print(','.join(a))
'''

# 4. find 함수
# find 함수는 입력한 문자열의 인덱스 번호 어디에 있는지를 반환해 주는 함수입니다
# find 함수는 인덱스 번호 0번 부터 문자열을 찾습니다
'''
a = 'hello'
b = 'My name is James'
print(a.find('ll'))
print(b.find('i'))
'''
# find 함수는 문자열을 찾을 수 없는 경우 무조건 -1을 반환합니다 -> 에러는 X, 실행은 O
'''
a = 'hello'
b = 'Hello my name is Kim'
print(a.find('a'))
print(a.find('L'))
print(b.find('AA'))
print(b.find('Lee'))
'''

# 5. rfind 함수
# rfind 함수는 find 함수와 효과는 동일하지만 차이점은 인덱스 번호 0번 부터 찾는 것이 아닌 -1번부터 찾습니다
'''
a = 'Hello, this is my home page'
print(a.rfind('l')) 
print(a.rfind('e'))
print(a.rfind('s'))
print(a.rfind('i'))    # 오른쪽에서 왼쪽으로 진행
'''

# 6. index 함수
# index 함수의 효과는 find 함수와 동일하나 차이점은 찾는 문자열이 없는 경우에 에러가 발생합니다 **
'''
a = 'hello'
print(a.index('h'))
print(a.index('a'))  # 에러
'''

# 7. replace 함수
# replace 함수는 문자열을 변경하고 싶을 때 사용하는 함수입니다
# replace(바꾸고 싶은 문자열, 변경할 문자열)
'''
a = 'hello'
a = a.replace('he','HE')
b = "My name is Lee"
b = b.replace('Lee','Kim')
print(a)
print(b)
'''

# 8. upper 함수
# upper 함수는 문자를 (소문자에서)대문자로 바꾸고 싶을 때 사용하는 함수입니다
'''
a = 'hello'
b = 'Learning Python'
print(a.upper())
print(b.upper())
'''

# 9. lower 함수 
# lower 함수는 문자를 (대문자에서)소문자로 바꾸고 싶을 때 사용하는 함수입니다
'''
a = 'HELLO'
b = "This is Python"
print(a.lower())
print(b.lower())
'''
# 10. rstrip 함수
# rstrip 함수는 문자열에서 가장 오른쪽에 있는 공백을 삭제하는 함수입니다
# len 함수를 통해서 삭제 여부를 확인할 수 있습니다
'''
a = 'hello '
print(len(a))
a = a.rstrip()
print(len(a))
'''















































