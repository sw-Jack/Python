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


dic = {}
cnt = 1
while True : 
    choice = input("\n-----------------\n1.ID 추가\n2.ID 수정\n3.ID 확인\n4.프로그램 종료\n-----------------\n번호 선택 >> ")
    if choice == '1' :
        userid = input("\n<ID 추가>\n추가할 ID 입력 : ")
        if userid not in dic.values() :
            dic[cnt] = userid
            cnt += 1
        else : 
            print("입력하신 아이디가 이미 존재합니다.\n")
    elif choice == '2' :
        updateid = input("\n<ID 수정>\n수정할 ID Key 나 ID 입력 : ")
        if updateid not in str(dic.keys()) and updateid not in dic.values() :
            print("입력하신 아이디 키가 존재하지 않습니다.\n")
            continue
        else :
            fixid = input("새 아이디 입력 : ")
            if fixid in dic.values() :
                print("입력 하신 아이디가 이미 존재합니다.\n")
            else :
                if updateid in str(dic.keys()) :
                    dic[int(updateid)] = fixid
                elif updateid in dic.values() :
                    for i in range(1, len(dic)+1) :
                        if dic[i] == updateid :
                            dic[i] = fixid
    elif choice == '3' :
        print(f'\n<ID 확인>\n{dic}\n')
    elif choice == '4' :
        print('\n프로그램 종료...')
        exit()
    else : 
        print("해당 번호가 존재하지 않습니다. 다시 입력하세요\n")
    
        







