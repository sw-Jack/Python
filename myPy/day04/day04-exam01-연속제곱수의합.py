# Quiz
# (1) 1부터 n까지 연속한 숫자의 제곱을 구하는 프로그램 (for문 사용)
# n = 10 이면 1*1 + 2*2 + 3*3 + ... + 10*10 = ? : 385, 이 알고리즘은 O(n)? or O(1)?


def sum_sq1(n) :
    sum = 0
    for i in range(1,n+1) :
        sum = sum + i*i
    return sum

print(sum_sq1(10))
print(sum_sq1(100))
        
# 위 함수의 시간 복잡도는 O(n) : for문이 돌 때, n만큼 더하기와 곱하기가 행해진다.
# 공식 : n(n+1)(2n+1) / 2
# 공식 이용 함수

def sum_sq2(n) :
    return  n*(n+1)*(2*n+1) // 6

print(sum_sq2(10))
print(sum_sq2(100))
