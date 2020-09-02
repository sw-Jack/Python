print()

# 리스트에서 사용할 수 있는 함수
# 1. append 함수
# 리스트에 요소값을 추가해주는 함수입니다
# append() 안에 추가하고 싶은 요소값을 입력합니다
# append는 리스트에 맨 뒤에 추가됩니다
'''
a = []
a.append(10)
print(a)
'''
'''
a = [1,2,3]
a.append([4,5,6])    # 리스트도 추가 가능
print(a)
'''

# 2. insert 함수
# 리스트의 요소값을 삽입할 때 사용하는 함수
# insert 는 append와 비슷한 효과를 가지고 있지만 insert 는 인덱스 번호를 사용하여 요소값을 추가할 수 있다.
'''
a = [1,2,3,4,5]
a.insert(0,10)   # 인덱스 0번에 정수 10 삽입
a.insert(2,'python')   # 인덱스 2번에  문자열 python 삽입
a.insert(-1,50)  # 음수 인덱싱도 사용 가능 
print(a)
'''

# 3. remove 함수
# remove 함수는 del과 동일한 효과를 가지고 있지만 remove는 요소값을 찾아서 삭제합니다
# remove는 리스트에서 가장 먼저 나오는 요소값만 삭제합니다
'''
a = [1,2,3]
print(a)
a.remove(1)     # 괄호 안에 요소값, 리스트에 있는 요소값 1을 삭제
print(a)
'''

'''
a = [1,2,3,4,3]
print(a)
a.remove(3)   # 왼쪽부터 검사하여 가장 먼저 나오는 대상을 삭제 ***
print(a)
 '''

# 4. pop 함수 **
# 리스트의 요소를 다른 변수나 리스트로 이동시켜 줄 수 있습니다
# 윈도우의 잘라내기 기능과 유사합니다
'''
a = [1,2,4,6,2,3]
b = a.pop(1)      # 인덱스 번호 1의 값 2를 변수 b에 저장 후 리스트에서 삭제
c = a.pop(4)      # 인덱스 번호 4의 값 3를 변수 c에 저장 후 리스트에서 삭제
print(a)
print(b)
print(c)
'''

# 5. sort 함수
# sort 함수는 리스트의 요소를 순차적으로 정렬하는 기능을 가지고 있는 함수입니다 : 오름차순
# 오름차순
'''
a = [1,10,89,25,22,13,5]
b = [100, 90, 80, 70, 60, 50]
c = ['d','r','e','g','a','b','h','c']   # 문자도 알파벳 순서로 정렬 가능
a.sort()
b.sort()
c.sort()
print(a);print(b);print(c)
'''
# 내림차순
'''
a = [1,10,89,25,22,13,5]
b = ['가','다','마','라','아','사,','나']  # 한글 문자도 정렬 가능
c = ['d','r','e','g','a','b','h','c']   # 문자도 알파벳 순서로 정렬 가능
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)
print(a);print(b);print(c)
'''

# 6. reverse 함수 
# reverse 함수는 리스트 안에 요소값을 거꾸로 뒤집는 기능을 가지고 있는 함수입니다
'''
a = [1,2,5,3,4]
b = ['10','8','6','4','2','0']
a.reverse()
b.reverse()
print(a);print(b)
'''

# 7. count 함수 
# count 함수는 리스트 안에 내가 입력한 요소값이 몇개가 포함되어 있는지 반환해주는 함수입니다
# 문자열에서 사용했던 형식과 동일합니다 
'''
a = [1,2,5,3,1]
b = ['python','Python','java','jsp']
print(a.count(1))        # 정수형 요소값
print(b.count('Python'))   # 문자열형 요소값
'''

# 8. index 함수
# index 함수는 입력한 요소값이 리스트의 어디에 저장되어 있는지 반환해주는 함수, 즉 인덱스 번호를 반환
'''
a = [1,2,3]
b = ['a','b','c','d','e']
print(a.index(3))    # 정수형 요소값 
print(b.index('d'))  # 문자형 요소값
# print(a.find(3))    # 리스트에서는 find 사용 불가
'''

# 9. extend 함수
# extend 함수는 리스트를 확장시켜주는 기능을 가지고 있습니다
# extend 안에는 리스트만 사용이 가능합니다
# 리스트 + 리스트 와 동일한 효과를 가지고 있습니다
'''
a = [1,2,3]
print(a)
a.extend([4,5])
print(a)
a.extend(['e','x','t','e','n','d'])
print(a)
'''

# 연습 문제
# ID 관리 프로그램 만들기
# ID는 일반 ID 그리고 VIP ID로 구분합니다
# ID는 절대 중복이 될 수 없습니다
# VIP ID는 반드시 일반 ID에서 승격을 시켜서 사용해야 합니다
# ID는 반드시 6글자 이상 사용해야 합니다
# 반드시 리스트를 사용합니다
# 아래와 같은 기능을 가지고 있어야 합니다
# 1. ID 목록 확인
# 2. ID 등록
# 3. ID 삭제
# 4. VIP 승격
# 5. 프로그램 종료

# import os
# os.system('cls')
# trash = input("계속하려면 엔터를 누르세요...")

'''
# 일반 id를 담을 리스트 생성
idlst = []
# vip id를 담을 리스트 생성
vipidlst = []
# 사용자가 강제로 프로그램을 종료하기 전에는 계속해서 프로그램이 돌아가도록 무한 루프 생성
while True :
    print("\n<ID 관리 프로그램>")
    # 5가지 기능 출력과 함께 사용자 입력 받기
    num = int(input("1.ID 목록 확인\n2.ID 등록\n3.ID 삭제\n4.VIP 승격\n5.프로그램 종료번호를 선택하세요 : "))
    # 1번 선택할 경우
    if num == 1 :
        # 일반 id 리스트와 vip id 리스트 출력
        print("\n<ID 목록 확인> : {}".format(idlst))
        print("<VIP ID 목록 확인> : {}\n".format(vipidlst))
    # 2번 선택할 경우
    elif num == 2 :
        # 원하는 경우에 빠져나올 수 있도록 조건문 내 무한 루프 생성
        while True :
            # 등록할 id 입력 받기
            inID = input("\n<ID 등록>\n등록할 ID 입력 (6자리 이상 입력): ")
            # 입력 받은 id가 조건대로 6자리 이상이면 
            if len(inID) >= 6 :
                # 입력 받은 id가 기존의 id 리스트와 vip id 리스트 모두에 존재하지 않는다면 등록 완료 후 무한 루프 탈출
                if inID not in idlst and inID not in vipidlst :
                    idlst.append(inID)
                    print("ID 등록 완료! 등록 ID 확인 : {}".format(inID))
                    break
                # 입력 받은 id가 기존의 id 리스트 혹은 vip id 리스트 둘 중 하나에라도 존재하면 다시 입력받도록 continue
                else :
                    print("해당 ID가 이미 존재합니다. 다시 입력하세요")
                    continue
            # 입력 받은 id가 조건과 다르게 6자리 미만이면 다시 입력 받도록 continue
            else :
                print("ID는 6자리 이상 입력되어야 합니다. 다시 입력하세요")
                continue
    # 3번 선택할 경우
    elif num == 3 :
        # 원하는 경우에 빠져나올 수 있도록 조건문 내 무한 루프 생성
        while True :
            # 삭제할 id 입력 받기
            outID = input("\n<ID 삭제>\n삭제할 ID 입력 : ")
            # 입력 받은 id가 기존의 id 리스트에 존재하는 경우
            if outID in idlst :
                # 삭제할 id 확인 시켜준 뒤 삭제, 무한 루프 탈출
                print("삭제할 ID : {}, 삭제 완료".format(outID))
                idlst.remove(outID)
                break
            # 입력 받은 id가 기존의 vip id 리스트에 존재하는 경우
            elif outID in vipidlst :
                # 삭제할 id 확인 시켜준 뒤 삭제, 무한 루프 탈출
                print("삭제할 ID : {}, 삭제 완료".format(outID))
                vipidlst.remove(outID)
                break
            # 입력 받은 id가 기존의 어느 리스트에도 존재하지 않는 경우 다시 입력 받도록 continue
            else : 
                print("삭제할 ID가 없습니다. 다시 입력하세요 ")
                continue
    # 4번 선택할 경우
    elif num == 4 :
        # 원하는 경우 빠져나올 수 있도록 무한 루프 생성
        while True :
            # 승격시킬 id 입력 받기
            vip = input("\n<VIP 승격>\n승격시킬 ID 입력 : ")
            # 입력 받은 id가 기존의 id 리스트에 존재할 경우
            if vip in idlst : 
                # 입력 받은 id를 id 리스트에서 삭제
                idlst.remove(vip)     
                # vip id 리스트에 입력 받은 id 추가            
                vipidlst.append(vip)
                # 승격 완료 문구 출력 후 무한 루프 탈출
                print("승격 완료! 승격 ID 확인: {}".format(vip))
                break
            # 입력 받은 id가 기존의 id 리스트에 존재하지 않을 경우 다시 입력 받도록 continue
            else :
                print("입력한 ID가 등록되어있지 않습니다")
                continue
    # 5번 선택할 경우 프로그램 종료 문구 출력 후 프로그램 종료
    elif num == 5 :
        print("프로그램 종료")
        break
    # 해당 번호 외 번호를 선택할 경우
    else :
        # 다시 입력하라는 문구 출력 후 다시 가장 처음으로 continue
        print("\n번호를 다시 입력하세요")
        continue
'''
'''
import os
normal=[] # 일반 ID 리스트
vip = [] # vip ID 리스트
while 1 :
    os.system('cls')
    print('''1.ID목록 확인
2.ID등록
3.ID삭제
4.VIP 승격
5.프로그램 종료''')
    choi = int(input("원하시는 항목을 입력하세요 : "))
    if choi == 1 :
        print("일반 ID :",normal)
        print("VIP ID :",vip)
        trash = input("계속하려면 엔터를 누르세요...")
    elif choi == 2 :
        name = input("추가하고 싶은 ID을 입력하세요 : ")
        if len(name) >= 6 :
            if normal.count(name) == 1 or vip.count(name) == 1:
                print("중복된 ID 입니다")
                trash = input("계속하려면 엔터를 누르세요...")
            else :
                normal.append(name)
                print("정상적으로 추가되었습니다")
                trash = input("계속하려면 엔터를 누르세요...")
        else :
            print("ID는 6글자 이상으로 만들어야 합니다")
            trash = input("계속하려면 엔터를 누르세요...")
    elif choi == 3 :
        print(normal)
        print(vip)
        name = input("삭제하고 싶은 ID를 입력하세요 : ")
        if normal.count(name) == 1 :
            normal.remove(name)
            print("삭제 되었습니다")
            trash = input("계속하려면 엔터를 누르세요...")
        elif vip.count(name) == 1:
            vip.remove(name)
            print("삭제 되었습니다")
            trash = input("계속하려면 엔터를 누르세요...")
        else :
            print("없는 계정입니다 다시 입력해주세요")
            trash = input("계속하려면 엔터를 누르세요...")           
    elif choi == 4:
        print(normal)
        name = input("승격시킬 ID를 입력하세요 : ")
        idx = normal.index(name)
        up = normal.pop(idx)
        vip.append(up)
        print("정상적으로 승격되었습니다!")
        trash = input("계속하려면 엔터를 누르세요...")
    elif choi == 5 :
        print("프로그램을 종료합니다")
        break
'''
 
