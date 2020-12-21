# 선택 정렬 (day04 마지막 코드)
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



# Quiz : 선택 정렬을 하는데, 오름차순이 아닌 내림차순으로 정렬하기
def select_sort(a) :
    n = len(a)
    for i in range(n-1) :
        max_idx = i
        for j in range(i+1,n) :
            if a[j] > a[max_idx] :
                max_idx = j
        a[i], a[max_idx] = a[max_idx], a[i]

print("\n--- 알고리즘 사용 ---")
data = [35,36,100,0,8,1,88,17,99,98,50,56,2]
select_sort(data)
print(data)
