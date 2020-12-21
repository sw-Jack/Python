# Quiz1
# n명을 입력하면 두 명을 뽑아 짝지어서 그 조합을 출력
# 예를 들어 ["Tom","Mike","Jerry"] 가 있을 때,
# Tom-Mike / Tom-Jerry
# Mike-Jerry 조합이 나온다.

def making_couple(lst) :
    n = len(lst)
    for i in range(n-1) :
        for j in range(i+1,n) :
            print(lst[i], "--", lst[j])
    


lst = ["Tom","Mike","Jerry"]
print(making_couple(lst))





# Quiz2
# 빅오 표기법으로 아래의 수식을 나타내면?
# (1) 65536 --> O(1)
# (2) n-1 --> O(n)
# (3) 2n^2/3 + 1000n --> O(n^2)
# (4) 3n^4 - 4n^3 + 5n^2 -6n + 7 --> O(n^4)
