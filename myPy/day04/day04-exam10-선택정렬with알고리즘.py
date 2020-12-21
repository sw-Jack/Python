# 정렬 : 선택, 삽입, 병합, ...
# (1) 선택 정렬
# - 주어진 리스트에서 작은 수부터 큰 수 순서대로 배열하는 정렬
# - 입력 : [35,8,1,88,17]
# - 출력 : [1,8,17,35,88]

# 일반 상식 코드
def find_min_idx(a) :
    n = len(a)
    min_idx = 0
    for i in range(1,n) :
        if a[i] < a[min_idx] :
            min_idx = i
    return min_idx
        
    
def select_sort(a) :
    res = []
    while a :
        min_idx = find_min_idx(a)
        value = a.pop(min_idx)
        res.append(value)
    return res

print("--- 일반 상식 ---")
data = [35,8,1,88,17]
print(select_sort(data))


# 알고리즘 사용 코드
def select_sort(a) :
    n = len(a)
    for i in range(n-1) :
        min_idx = i
        for j in range(i+1,n) :
            if a[j] < a[min_idx] :
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

print("\n--- 알고리즘 사용 ---")
data = [35,36,100,0,8,1,88,17,99,98,50,56,2]
select_sort(data)
print(data)
    
