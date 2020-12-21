# 입력한 n에 대해 계산 횟수가 정비례 --> O(n)
def sum_n1(n) :
    sum = 0
    for i in range(1,n+1) :
        sum += i
    return sum

# 입력한 n과 관계없이 사친연산 세번 수행 --> O(1)
def sum_n2(n) :
    return n * (n+1) // 2


print(sum_n1(10))
print(sum_n1(100))
print()
print(sum_n2(10))
print(sum_n2(100))

