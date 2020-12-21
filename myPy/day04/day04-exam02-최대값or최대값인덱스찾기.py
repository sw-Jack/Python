# 최댓값 찾기 : 주어진 숫자 n개 중에서 가장 큰 값을 찾는 것

# 리스트 사용
# lst = [5,7,9]
# print(max(lst))

# 함수 사용
def find_max(a) : # a는 리스트로 값의 목록
    n = len(a)
    maxVal = a[0]
    for i in range(1,n) :
        if a[i] > maxVal :
            maxVal = a[i]
    return maxVal

value = [17,18,92,33,105,77,21,8]
print(find_max(value))





# 추가 Quiz : 주어진 숫자 n(리스트)을 주면 최대값의 index를 출력하는 것
def find_maxIdx(a) :
    n = len(a)
    maxIdx = 0
    for i in range(1,n) :
        if a[i] > a[maxIdx] :
            maxIdx = i
    return maxIdx
value = [17,18,92,33,105,77,21,8,200]
print(find_maxIdx(value))



