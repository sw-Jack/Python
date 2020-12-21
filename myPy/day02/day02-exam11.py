# def 함수이름(인자) :
#       함수 내용
#       return 함수의 결과

# def hello(name) :
#   print("Hello!", name)

# hello("손오공")
# hello("사오정")
# hello("홍길동")

# def square(a) :
#     c = a * a
#     return c

# def = triangle(a, h) :
#     c = a * h / 2
#     return c 


# 함수 이름은 sum_func
# sum_func는 숫자 n을 받아서 0부터 숫자 n까지 합을
# 구해서 리턴해주는 함수입니다.
def sum_func(n) :
    sum = 0
    for x in range(n+1) :
        sum += x
    return sum


print(sum_func(10))
