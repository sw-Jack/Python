# 최소값 구하는 프로그램
def min(lst) :
    a = len(lst)
    minVal = lst[a-1]
    for i in range(1,a) :
        if lst[i] < minVal :
            minVal = lst[i]
    return minVal

exlst = [10,43,46,2,100,12,9,78]
print(min(exlst))


         
