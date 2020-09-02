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

import os
Idlst = []
Viplst = []
while(1) :
    os.system("cls")
    menu = input("<메뉴>\n1.ID 목록 확인\n2.ID 등록\n3.ID 삭제\n4.VIP 승격\n5.프로그램 종료\n번호 선택 >> ")
    if menu == '1' :
        whatlst = input("\n<ID 목록 확인>\n1.일반 ID 목록\n2.VIP ID 목록\n번호 선택 >> ")
        if whatlst == '1' :
            print(f'\n[일반 ID 목록]\n{Idlst}\n') 
            trash = input('계속하려면 엔터키를 누르세요...') 
        elif whatlst == '2' :
            print(f'\n[Vip ID 목록]\n{Viplst}\n') 
            trash = input('계속하려면 엔터키를 누르세요...') 
    elif menu == '2' :
        while True : 
            enid = input('\n<아이디 등록>\n아이디 입력(6자리 이상) : ')
            if len(enid) >= 6 :
                if enid not in Idlst and enid not in Viplst :
                    Idlst.append(enid)
                    print(f'입력 아이디 : {enid}\n아이디가 성공적으로 등록되었습니다! 반갑습니다 {enid}님^^\n')
                    trash = input('계속하려면 엔터키를 누르세요...') 
                    break
            else : 
                print('아이디는 6자리 이상 입력해야 합니다...')
    elif menu == '3' :
        while True :
            rmid = input('\n<아이디 삭제>\n삭제할 아이디 입력 : ')
            if (Idlst.count(rmid) + Viplst.count(rmid)) >= 1 :
                rmquestion = input(f'입력 아이디 : {rmid}, 정말 삭제하시겠습니다까? (y/n) : ')
                if rmquestion == 'y' :
                    if Idlst.count(rmid) == 1 :
                        Idlst.remove(rmid)
                    elif Viplst(rmid) == 1 :
                        Viplst.remove(rmid)
                    print('아이디가 삭제되었습니다!\n')
                    trash = input('계속하려면 엔터키를 누르세요...') 
                    break
                else :
                    trash = input('계속하려면 엔터키를 누르세요...') 
                    break
            else : 
                print('입력하신 아이디가 존재하지 않습니다.\n')
                trash = input('계속하려면 엔터키를 누르세요...') 
                break
    elif menu == '4' :
        while True :
            upid = input('\n<VIP 승격>\n승격시킬 아이디 입력 : ')
            if upid in Idlst : 
                upquestion = input(f'승격시킬 아이디 : {upid}, 정말 승격시키시겠습니다? (y/n) : ')
                if upquestion == 'y' :
                    Viplst.append(upid)
                    Idlst.remove(upid)
                    print(f'승격 완료 되었습니다! new Vip ID : {upid}')
                    trash = input('계속하려면 엔터키를 누르세요...') 
                    break
                else : 
                    trash = input('계속하려면 엔터키를 누르세요...') 
                    break
            else : 
                print('해당 아이디가 존재하지 않습니다...\n')
    elif menu == '5' :
        print('프로그램 종료...\n')
        exit()

                    
