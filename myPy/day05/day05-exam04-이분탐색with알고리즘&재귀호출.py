# 이분 탐색
# 자료가 이미 정렬되어 있다는 전제.
# 자료가 있으면 위치값을 알려주고 없으면 -1

# 알고리즘
# (1) 중간 위치를 찾는다
# (2) 찾는 값과 중간 위치의 값을 비교한다.
# (3) 같으면 해당 값의 위치를 반환한다
# (4) 찾는 값이 중간 값보다 크다면 중간 값 기준 오른쪽을 대상으로 다시 검색한다.
# (5) 찿는 값이 중간 값보다 작다면 중간 값 기준 왼쪽을 대상으로 다시 검색한다.



# 코드
def binary_search(lst,x) :
    start = 0
    end = len(lst) - 1

    while start <= end :
        mid = (start + end) // 2
        if x == lst[mid] :
            return mid
        elif x > lst[mid] :
            start = mid + 1
        else :
            end = mid - 1
    return -1

data = [1,4,9,16,25,36,49.64,81]
print(binary_search(data,36))
print(binary_search(data,4))
print(binary_search(data,90))




# Quiz : 재귀 호출을 이용한  이분 탐색 구현
# (1) 주어진 탐색 대상이 비어있다면 탐색할 필요가 없다.(종료)
# (2) 찾는 값과 중간 값을 비교한다.
# (3) 찾는 값과 중간 값이 같으면 해당 값의 위치를 반환한다
# (4) 찾는 값이 중간 값보다 크다면 중간 값 기준 오른쪽을 대상으로 이분 탐색 재귀 호출을 실행한다.
# (5) 찿는 값이 중간 값보다 작다면 중간 값 기준 왼쪽을 대상으로 이분 탐색 재귀 호출을 실행한다.

# 코드
def binary_search_sub(a,x,start,end) :
    if start > end :
        return -1
    mid = (start + end) // 2

    if x == a[mid] :
        return mid
    elif x > a[mid] :
        return binary_search_sub(a,x,mid+1,end)
    else :
        return binary_search_sub(a,x,start,mid-1)
    return -1

def binary_search(a,x) :
    return binary_search_sub(a,x,0,len(a)-1)
    

data = [1,4,9,16,25,36,49.64,81]
print(binary_search(data,36))
print(binary_search(data,4))
print(binary_search(data,90))
































    
