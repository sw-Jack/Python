# n까지 곱하는 함수, 팩토리얼 함수
def factorial(n) :
    fact = 1
    for i in range(1,n+1) :
        fact = fact * i
    return fact

print(factorial(5))
