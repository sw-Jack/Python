# 동명이인 찾기 with 딕셔너리
# - 알고리즘
# (1) 각 이름이 등장하는 횟수를 저장할 빈 딕셔너리를 작성한다.
# (2) 입력으로 주어진 리스트에서 각 이름을 꺼내면서 반복한다.
# (3) 주어진 이름이 name_dict에 있는지 확인한다.
# (4) 있다면 횟수를 +1, 없다면 key 값으로 이름을 추가한다.
# (5) 위 과정을 반복한다.
# (6) 횟수가 2이상인 것만 따로 추출한다.

# 코드
def find_same_name(lst) :
    name_dict = {}

    for name in lst :
        if name in name_dict :
            name_dict[name] += 1
        else :
            name_dict[name] = 1

    res = set()
    for name in name_dict :
        if name_dict[name] >= 2 :
            res.add(name)
    return res

name1 = ["Tom","Jerry","Mike","Tom"]
print(find_same_name(name1))
name2 = ["Tom","Jerry","Mike","Tom","Jerry"]
print(find_same_name(name2))
print()


# Quiz : 학생 번호로 학생 이름 찾기 with 딕셔너리
# 39 : Justine / 14 : John / 20 : Stone / 68 : Mike / 100 : Summer
def find(info, stu_no) :
    if stu_no in info :
        return info[stu_no]
    return "뉴규??"

stu_info = { 39 : 'Justine', 14 : 'John', 20 : 'Stone', 68 : 'Mike', 100 : 'Summer' }
print(find(stu_info, 39))
print(find(stu_info, 101))
































    
