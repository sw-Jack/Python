print()
# 딕셔너리에서 사용할 수 있는 함수 
# 3. values 함수
# values 함수는 딕셔너리 안에서 value 에 해당하는 값만 모아서 객체 형태로 반환해주는 함수입니다
'''
a = {'이름' : '박지성', '나이' : 38, '취미' : '축구'}
b = {100 : 1, 200 : 2, 300 : 3}
print(a.values())          # 객체 형태로 반환
print(b.values())          # 객체 형태로 반환
print(list(a.values()))    # 리스트 형태로 반환
print(list(b.values()))    # 리스트 형태로 반환
'''

# 4. items 함수
# items 함수는 딕셔너리 안에서 key 와 value 값을 하나의 튜플 형태로 저장한 후 객체 형태로 반환해주는 함수입니다
'''
a = {'이름' : '홍길동', '나이' : 20, '직업' : '프로그래머'}
b = {1 : 100, 2 : 200, 3 : 300}
print(a.items())          # 객체 형태로 반환
print(b.items())          # 객체 형태로 반환
print(list(a.items()))    # 리스트 형태로 반환
print(list(b.items()))    # 리스트 형태로 반환
'''

# 5. in 함수
# in 은 입력한 key 값이 딕셔너리 안에 있는지 찾아주는 함수입니다
'''
a = {'이름' : '홍길동', '나이' : 20, '취미' : '독서'}
b = {1 : '대한민국', 2 : '미국', 3 : '일본'}
print('이름' in a)   # 있으면 True
print('특기' in a)   # 없으면 False
print(1 in b);print(2 in b)
print('주소' not in a)
print(3 not in b)
'''


# 6. clear 함수
# clear 함수는 딕셔너리를 초기화시키는 기능을 가지고 있습니다
'''
a = {'이름' : '홍길동', '나이' : 20, '취미' : '독서', '주소' : '강남구'}
print(a)
a.clear()
print(a)
'''

# 딕셔너리 연습 문제 
# 사용자가 직접 ID를 입력해서 딕셔너리 안에 값이 들어가는 프로그램
# 1. ID 추가
# - 사용자가 ID를 지정하면 자동으로 key는 1로 지정
# - 사용자가 추가될 때마다 key는 자동으로 2,3,4 순으로 지정
# 2. ID 수정
# - ID 명단의 ID를 수정할 때에는 해당 key값을 입력받습니다
# - key값을 입력받으면 그에 해당하는 value를 변경할 ID를 입력합니다(수정할 ID)
# 3. ID 확인
# - 딕셔너리 출력
# 4. 프로그램 종료
'''
dict = {}
key = 1
while True :
    tex = int(input("\n<프로그램 실행>\n(1)ID 추가\n(2)ID 수정\n(3)ID 확인\n(4)프로그램 종료\n번호 입력 : "))
    if tex ==  1 :
        while True :
            inid = input("\n<ID 추가>\n추가할 ID 입력 : ")
            if inid not in dict :
                dict[key] = inid
                key += 1
                print("ID 추가 완료, 추가한 ID : {}\nID 목록 : {}".format(inid,dict))
                break
            else :
                continue
    elif tex == 2 :
        while True :
            fixkey = int(input("\n<ID 수정>\n수정할 ID key 입력 : "))
            if fixkey not in dict :
                print("수정할 ID key가 목록에 없습니다. 다시 입력하세요")
                continue
            else :
                fixid = input("수정할 ID 입력 : ")
                dict[fixkey] = fixid
                print("ID 수정 완료, 수정한 ID : {}\nID 목록 : {}".format(fixid,dict))
                break
    elif tex == 3 :
        print("\n<ID 확인>\nID 목록 : {}".format(dict))
    elif tex == 4 :
        print("프로그램 종료")
        break 
    else : 
        print("번호를 다시 입력하세요")
        continue
'''



# 딕셔너리 연습 문제 
# 사용자가 직접 ID를 입력해서 딕셔너리 안에 값이 들어가는 프로그램
# 1. ID 추가
# - 사용자가 ID를 지정하면 자동으로 key는 1로 지정
# - 사용자가 추가될 때마다 key는 자동으로 2,3,4 순으로 지정
# - ID는 최대 5개 까지 만들 수 있습니다   ******
# 2. ID 수정
# - ID 명단의 ID를 수정할 때에는 해당 key값을 입력받습니다
# - key값을 입력받으면 그에 해당하는 value를 변경할 ID를 입력합니다(수정할 ID)
# - 추가적으로 key 값 뿐만 아니라 ID를 입력해도 똑같이 ID를 변경할 수 있도록 만들어주세요  *******
# 3. ID 확인
# - 딕셔너리 출력
# 4. 프로그램 종료     
'''
dict, key = {}, 1
while True :
    tex = input("\n<프로그램 실행>\n(1)ID 추가\n(2)ID 수정\n(3)ID 확인\n(4)프로그램 종료\n번호 입력 : ")
    if tex ==  '1' :
        if key > 5 :
            print("더이상 ID를 추가할 수 없습니다")
            continue
        while True :
            inid = input("\n<ID 추가>\n추가할 ID 입력 : ")
            if inid not in dict :           
                dict[key] = inid
                key += 1
                print("ID 추가 완료, 추가한 ID : {}\nID 목록 : {}".format(inid,dict))
                break
            else :
                print("입력한 ID가 이미 존재합니다. 다시 입력하세요")
                continue
    elif tex == '2' :
        while True :
            fixkey = input("\n<ID 수정>\n수정할 ID 혹은 ID key 입력 : ")
            if fixkey not in str(dict.keys()) and fixkey not in dict.values() :
                print("수정할 ID key가 목록에 없습니다. 다시 입력하세요")
                continue
            else :
                fixid = input("변경 ID 입력 : ")
                if fixkey in dict.values() :
                    for a in range(1,len(dict)+1) :
                        if dict[a] == fixkey : 
                            dict[a] = fixid                             
                elif fixkey in str(dict.keys()) :
                    dict[int(fixkey)] = fixid
                print("ID 수정 완료, 수정한 ID : {}\nID 목록 : {}".format(fixid,dict))
                break
    elif tex == '3' :
        print("\n<ID 확인>\nID 목록 : {}".format(dict))
    elif tex == '4' :
        print("프로그램 종료")
        break 
    else : 
        print("번호를 다시 입력하세요")
        continue  
'''



# 딕셔너리 연습 문제
# 사용자가 직접 ID를 입력해서 딕셔너리 안에 값이 들어가는 프로그램을 만들어주세요
# 1.ID 추가
#   -사용자가 ID를 지정하면 자동으로 key 는 1로 지정
#   -사용자가 추가 될 때마다 key는 자동으로 2,3,4 순으로 지정이 됩니다
#   -ID는 최대 5개 까지 만들수 있습니다
# 2.ID 수정
#   -ID 명단의 ID를 수정 할 때에는 해당 Key값을 입력 받습니다
#   -key 값을 입력받으면 그에 해당하는 value를 변경 할 ID를 입력합니다(수정 할 ID) 
#   -추가적으로 Key 값 뿐만 아니라 ID를 입력해도 똑같이 ID를 변경 할 수 있도록 만들어주세요
# 3. ID 확인
#   -딕셔너리 출력
# 4. 프로그램 종료
'''
name = {}
chkey = 1
while 1 :
    print("""1.ID추가
2.ID수정
3.ID확인
4.ID삭제""")
    num = int(input("원하시는 번호를 입력해주세요 : "))
    if num == 1 :
        if chkey > 5 : 
            print("ID를 더이상 추가할 수 없습니다")           
        a = input("추가하고 싶은 ID를 입력하세요 : ")
        name[chkey] = a
        chkey = chkey + 1
        print(name)
    elif num == 2 :
        print(name)
        a = input("ID의 번호나 ID를 입력하세요 : ")
        if a in list(name.values()) :
            chid = input("바꾸고 싶은 ID를 입력하세요 :")
            b = list(name.values())
            count = 0
            for c in b :
                count = count+1
                if c == a :
                    name[count] = chid
                    print(name)
        elif int(a) in list(name.keys()) :
            chID = input("바꾸고 싶은 ID를 입력하세요 : ")
            name[int(a)] = chID
            print(name)
        else :
            print("다시 입력하세요")
    elif num == 3 :
        print(name)
    elif num == 4 :
        print("프로그램을 종료 합니다")
        break
'''
































