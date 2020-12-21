# 팩토리얼 구하기

def factorial(n) :
    fact = 1
    for i in range(1,n+1) :
        fact *= i
    return fact

print(factorial(5))


# 재귀 호출 : 어떤 함수가 자기 자신을 부르는 함수
# --> 주의할 점 : 종료 조건이 반드시 필요하다.

# 알고리즘
# 1! = 1                    
# 2! = 2 * 1                = 2 * 1!
# 3! = 3 * 2 * 1            = 3 * 2!
# 4! = 4 * 3 * 2 * 1        = 4 * 3!
# 5! = 5 * 4 * 3 * 2 * 1    = 5 * 4!
# ...
#                           결국 --> n! = n * (n-1)!


# 재귀 사용

def factorial(n) :
    if n <= 1 :
        return 1
    return (n * factorial(n-1))
print(factorial(5))

