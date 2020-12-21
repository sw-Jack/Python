# 병합 정렬
def merge_sort1(a) :
    n = len(a)
    if n <= 1 :
        return a

    mid = n // 2
    g1 = merge_sort1(a[:mid])
    g2 = merge_sort1(a[mid:])

    res = []
    while g1 and g2 :
        if g1[0] < g2[0] :
            res.append(g1.pop(0))   # pop으로 지워지면서 다음 인덱스가 [0]으로
        else :
            res.append(g2.pop(0))

    while g1 :
        res.append(g1.pop(0))
    while g2 :
        res.append(g2.pop(0))

    return res
            
data = [6,8,3,9,10,1,2,4,7,5]
print(merge_sort1(data))



# 다른 Version
def merge_sort(a) :
    n = len(a)

    if n <= 1:
        return

    mid = n // 2
    g1 = a[:mid]
    g2 = a[mid:]

    merge_sort(g1)
    merge_sort(g2)

    i1 = 0
    i2 = 0
    ia = 0
    while i1 < len(g1) and i2 < len(g2) :
        if g1[i1] < g2[i2] :
            a[ia] = g1[i1]
            i1 += 1
            ia += 1
        else :
            a[ia] = g2[i2]
            i2 += 1
            ia += 1

    while i1 < len(g1) :
        a[ia] = g1[i1]
        i1 += 1
        ia += 1
    while i2 < len(g2) :
        a[ia] = g2[i2]
        i2 += 1
        ia += 1

data = [6,8,3,9,10,1,2,4,7,5]
merge_sort(data)
print(data)























        














    
    
