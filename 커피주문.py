userTotmoney = 10000
americano, macchi, can = 3000, 4000, 500
menu = ['아메리카노','카라멜 마끼아또','캔','선택완료/종료', '1', '2', '3', '4']
while True :
    cntA, cntM, cntC = 0, 0, 0
    costTot = 0
    while True : 
        userSelect = input(f'\n@ Jack\'s Coffee @\n1.{menu[0]}\n2.{menu[1]}\n3.{menu[2]}\n4.{menu[3]}\n>> 메뉴선택 : ')
        if userSelect in menu :
            if userSelect == menu[0] or userSelect == menu[4] :
                cntA += 1
                costTot += americano
            elif userSelect == menu[1] or userSelect == menu[5] :
                cntM += 1
                costTot += macchi
            elif userSelect == menu[2] or userSelect == menu[6] :
                cntC += 1
                costTot += can
            else :
                break;    
        else : 
            print('해당 메뉴가 존재하지 않습니다. 다시 입력 하세요...')
    if cntA != 0 :
        print(f'아메리카노 : {cntA}개')
    if cntM != 0 :
        print(f'카라멜 마끼아또 : {cntM}개')
    if cntC != 0 :
        print(f'캔 : {cntC}개')
    if costTot > 0 : 
        print('주문완료! 결제 페이지로 이동...\n\n<주문내역>')
        ques1 = input(f'총 결제 금액 : {costTot}원...결제하시겠습니까(y/n) ')
        if ques1 == 'y' :
            if costTot > userTotmoney : 
                print(f'잔액 부족!! {costTot-userTotmoney}원이 모자랍니다!')
                continue
            else :
                print(f'결제 완료!! 카드 잔액 : {userTotmoney-costTot}원...')
                break
    ques2 = input('\n메뉴 재선택..아무키나 입력하세요(나가기 q)\n>> ')
    if ques2 == 'q' :
        print('안녕히 가세요^^')
        exit()

    




