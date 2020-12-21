# Quiz
# 1. 1부터 n까지의 합 구하기를 재귀 호출로 만들기
# 2. 숫자 n개 중 최대값 찾기를 재귀 호출로 만들기
# 3. 0과 1부터 시작해서 바로 앞으로 두 수를 더한 값을
# 다음 값으로 추가하는 방식으로 만든 수열을 피보나치 수열이라 한다.
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, ...
# n번째 피보나치 수를 구하는 알고리즘을 재귀 호출을 이용해서 만들어봐라
# 힌트 : 7번값 = 5번값 + 6번값

# 1번
def sum_n(n) :
    if n == 0 :
        return 0
    return sum_n(n-1) + n

print(sum_n(10))


# 2번
def find_max(a,n) :
    if n == 1 :
        return a[0]
    max_n_1 = find_max(a,n-1)
    if max_n_1 > a[n-1] :
        return max_n_1
    else :
        return a[n-1]

v = [17,21,92,55,36]
print(find_max(v,len(v))


# 3번
def fibo(n) :
    if n <= 1 :
        return n
    return fibo(n-1) + fibo(n-2)

for i in range(11) :
    print(fibo(i))






















      
