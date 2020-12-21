# 순차 탐색 : 주어진 리스트에서 특정한 값이 있는지 검색해서
# 그 위치값을 넘겨주는 프로그램
# [17,22,93,56,78,85,41]
# 56 ----> 3의 위치
# 단, 없으면 -1 반환

# a라는 리스트에서 x의 위치값 찾아내는 함수
def search_list(a,x) :
    n = len(a)
    for i in range(0,n) :
        if x == a[i] :
            return i
    return -1

v = [17,0,22,93,56,78,22,85,41,101,88,0,5,5]
print(search_list(v,41))
print(search_list(v,0))
print(search_list(v,17))
print(search_list(v,102))
print()

# Quiz1
# (1) 위의 순차 탐색은 앞에서 값을 찾으면 그 값의 위치만 알려준다.
# 해당하는 값이 여러 개 존재하는 경우, 모든 값의 위치를 리스트로 반환해주는
# 함수를 만들어보자.

# (2) 학생 번호와 이름이 리스트로 주어졌을 때, 학생 번호를 입력하면 이에
# 해당하는 이름을 순차 탐색하여 반환해주는 함수를 만들어보자
# ex)
# stu_no = [33,14,76,100]
# stu_name = ["홍길동","손오공","사오정","저팔계"]
# 33 ----> 홍길동
# 77 ----> 누구?

# 1번
def search(a,x) :
    newlst = []
    n = len(a)
    for i in range(n) :
        if x == a[i]:
            newlst.append(i)
    return newlst

print("----------------------\n<1번>")
lst = [5,17,0,22,93,56,78,22,85,5,41,101,88,0,5,5]
print(search(lst,41))
print(search(lst,0))
print(search(lst,5))
print(search(lst,102))
print()


# 2번
def get_name(stu_no, stu_name, find_no) :
    a = len(stu_no)
    for i in range(a) :
        if find_no == stu_no[i] :
            return stu_name[i]
    return "뉴규?"

print("----------------------\n<2번>")
stu_no = [33,14,76,100]
stu_name = ["홍길동","손오공","사오정","저팔계"]
print(get_name(stu_no, stu_name, 33))
print(get_name(stu_no, stu_name, 100))
print(get_name(stu_no, stu_name, 76))
print(get_name(stu_no, stu_name, 30))












































































            
