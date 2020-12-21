# 동명이인 찾기 : n명의 사람 이름 중에서 같은 이름을 찾아서

# 집합으로 만들어 돌려주는 프로그램

# ["홍길동","사오정","저팔계","손오공","사오정"]
# 집합은 리스트처럼 정보를 여러개 저장할 수 있는 파이썬의 기능이다
# 집합(set)의 특징은 자료의 중복이 허용되지 않는다는 것
# 집합(set)의 특징은 순서도 없다는 것

s = set()
s.add(1)
s.add(2)
s.add(3)
s.add(3)
s.add(4)
print(s)

# discard(value) : 집합(set)에서 해당 값(value) 삭제
s.discard(2)
print(s)



# set을 함수로 작성
# 입력은 리스트로 
# 첫번째에 있는 홍길동을 뒤에 있는 사오정, 저팔계 등과 차례대로 비교한다.
# 마지막에 있는 홍길동과 이름이 같으므로 동명이인이다. 이 값을 set으로 저장한다.
# 두번째 ... 반복 : 마지막 빼고
# 저장해놓은 set을 리턴해주고 출력한다.

def find_same(lst) :
    n = len(lst)
    res = set()
    for i in range(n-1) :
        for j in range(i+1,n) :
            if lst[i] == lst[j] :
                res.add(lst[i])
    return res
    
    

namelst = ["홍길동","사오정","저팔계","손오공","사오정","홍길동","저팔계","홍길동","손흥민"]
print(find_same(namelst))

# 시간 복잡도 : O(n^2)
