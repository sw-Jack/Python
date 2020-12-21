# 삽입 정렬
def find_ins_idx(r,v) :
    for i in range(len(r)) :
        if v < r[i] :
            return i
    return len(r)

def insert_sort(a) :
    res = []
    while a :
        val = a.pop(0)
        ins_idx = find_ins_idx(res,val)
        res.insert(ins_idx,val)
    return res

# data = [2,4,5,1,3]
data = [77,33,55,66,25,97,100,26]
print(insert_sort(data))


# 알고리즘
# i = 1     [2,4,5,1,3]     [2,4]
# i = 2     [2,4,5,1,3]     [2,4,5]
# i = 3     [2,4,5,1,3]     [1,2,4,5]
# i = 4     [2,4,5,1,3]     [1,2,3,4,5]


# 알고리즘 사용
def insert_sort(a) :
    n = len(a)
    for i in range(1,n) :   # 첫번째[0] 제외 두번째 원소[1]부터
        key = a[i]
        j = i - 1           # j는 key의 앞 수  (j,key) 순서 
        while j >= 0 and a[j] > key :
            a[j+1] = a[j]
            j -= 1
        a[j+1] = key
        
data = [2,4,5,1,3]
insert_sort(data)
print(data)
    
