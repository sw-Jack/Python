from random import *

while True :
    win, lose, draw, cnt, = 0, 0, 0, 0 
    tot = '무승부'
    print('\n<가위 바위 보 게임>')
    while True :
        status = '승'
        com = randint(1,3)
        user = input('가위/바위/보 중 선택 : ')
        if com == 1 :   # 컴퓨터 : 가위 -> 유저 : 가위(무) / 바위(승) / 보(패)
            com = '가위'
            if user == '가위' :
                status = '무'
                draw += 1
            elif user == '바위' :
                win += 1
            elif user == '보' :
                status = '패'
                lose += 1
            else : continue
        elif com == 2 :   # 컴퓨터 : 바위 -> 유저 : 가위(패) / 바위(무) / 보(승)
            com = '바위'
            if user == '가위' :
                status = '패'
                lose += 1
            elif user == '바위' :
                status = '무'
                draw += 1
            elif user == '보' :
                win += 1
            else : continue    
        else :   # 컴퓨터 : 보 -> 유저 : 가위(승) / 바위(패) / 보(무)
            com = '보'
            if user == '가위' :
                win += 1
            elif user == '바위' :
                status = '패'
                lose += 1
            elif user == '보' :
                status = '무'
                draw += 1
            else : continue
        # 게임 수 증가  +1
        cnt += 1
        # 매번 전적 출력
        print(f'[유저] {user} vs {com} [컴퓨터] >> {status} !!\n현재 : {win}승 {draw}무 {lose}패\n')
        # 5판3선승에 대한 총 결과 승무패 출력
        if win == 3 or lose == 3 or cnt >= 5 :
            print('\n5판 3선승제!!', end=' ')
            if win == 3 :
                tot = '유저 승'
                print('유저 3선승!\n')
                break
            elif lose == '3' :
                tot = '컴퓨터 승'
                print('컴퓨터 3선승!\n')
                break
            elif cnt >= 5 :
                print('5판 경과!')
                if win > lose :
                    tot = '유저 승'
                    break
                elif win < lose :
                    tot = '컴퓨터 승'
                    break
    print(f'\n<게임 종료...>\n총 결과 : {win}승 {draw}무 {lose}패\n{tot}!!\n')
    # 재실행 질문
    question = input('다시 하시겠습니까? (y/n) : ')
    if question == 'y' :
        continue
    else :
        print('Bye Bye ~!')
        break




   