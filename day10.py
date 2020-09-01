print("\n")
#2. 현재 사용자가 가지고 있는 돈은 10000원입니다
#사용자는 커피를 사려고 하는데 아이스아메리카노는 3000원, 
#카라멜 마끼아또는 4000원,
#캔 커피는 500원입니다
#사용자에게 어떤 것을 마실지 입력을 받아서 구매를 하고 만약 잔액이 부족하다면 "잔액부족" 이라는 문구가 나오도록 만들어주기
#조건 : 사용자가 입력할 때 번호 혹은 커피의 이름으로 입력을 해도 정상적으로 작동할 수 있도록 합니다
#조건 : 커피를 산 후 다시 커피를 살 수 있는 항목이 자동으로 나와야 합니다
#조건 : 사용자가 프로그램을 종료할 수 있어야 합니다
'''
money, americano, caramel, can = 10000, 3000, 4000, 500
while True :
    sum = 0
    cnt1, cnt2, cnt3 = 0, 0, 0
    while True :   
        tot = 0
        coff = input("<커피 선택>\n1.아메리카노\n2.카라멜 마끼아또\n3.캔커피\n4.종료\n주문 : ")
        if coff == '아메리카노' or coff == '1'  :
            print("\n아메리카노 구매, 가격 : {}\n".format(americano))
            sum += americano
            cnt1 += 1 
        elif coff == '카라멜 마끼아또' or coff == '2'  :
            print("\n카라멜 마끼아또 구매, 가격 : {}원\n".format(caramel))
            sum += caramel
            cnt2 += 1
        elif coff == '캔커피' or coff == '3'  :
            print("\n캔커피 구매, 가격 : {}원\n".format(can))
            sum += can
            cnt3 += 1
        elif coff == '4' :
            tot = tot + sum
            break
        else : 
            print("\n메뉴에 없습니다. 다시 입력 하세요\n")
    print("\n<주문 내용>")
    if cnt1 != 0 :
            print("아메리카노 {}개".format(cnt1))
    if cnt2 != 0 :
            print("카라멜 마끼아또 {}개".format(cnt2))
    if cnt3 != 0 :
            print("캔커피 {}개".format(cnt3))
    if tot > money :
        print("주문 총액 : {}원, 잔액 부족! {}원이 부족합니다\n".format(tot,tot-money))
    else :     
        print("구매 완료!\n총액 : {}원\n".format(tot))
        break
'''

'''
money, ice, caramel, can = 10000, 3000, 4000, 500
while True : 
    print("1.아이스 아메리카노")
    print("2.카라멜 마끼아또")
    print("3.캔커피")
    print("4.종료")
    choi = int(input("어떤 커피를 구매하시나요? "))
    if choi == '1' or '아이스 아메리카노' :
        if money >= ice :
            money = money - ice
            print("\n구매 완료! 현재 잔액은 %d입니다" %money)
        else :
                print("잔액 부족! 현재 잔액은 %d입니다" %money)       
    elif choi == '2' or '카라멜 마끼아또' :
        if money >= caramel :
            money = money - caramel
            print("\n구매 완료! 현재 잔액은 %d입니다" %money)
        else :
                print("잔액 부족! 현재 잔액은 %d입니다" %money)
    elif choi == '3' or '캔커피' :
        if money >= can :
            money = money - can
            print("\n구매 완료! 현재 잔액은 %d입니다" %money)
        else :
                print("잔액 부족! 현재 잔액은 %d입니다" %money)
    elif choi == '4' or '종료' :
        print("프로그램을 종료합니다")
        break
'''


#3. 1 ~ 100 까지의 누적합을 구하는 프로그램
'''
st = 0
sum = 0
while st <= 100 :
    sum += st
    st += 1
print(sum)
'''
'''
st = 1
sum = 0
while st < 101 :
    sum += st
    st += 1
print(sum)
'''


# 연습 문제
#1. 1 ~ x 의 범위에서 3과 5의 공배수의 합을 출력하는 프로그램
#조건 : x는 사용자 입력
'''
x = int(input("x값 입력 : "))
num = 1
sum = 0
while num <= x :
    if num%15 == 0 :                                         # num%3 == 0 and num%5 == 0
        sum += num
    num += 1
print("1 ~ {} 범위 내 3과 5의 공배수 합 : {}".format(x,sum))
'''



#2. 사용자가 입력한 값을 초과하지 않는 한도에서의 누적합을 구하는 코드 작성
#누적할 값은 랜덤으로 1 ~ 10 까지 생성
#조건 : 출력 결과는 반복 횟수와 값이 같이 나와야 합니다
'''
from random import *
userin = int(input("누적합의 한도 입력 : "))
sum = 0
cnt = 0
while sum <= userin :
    rand = randint(1,10)
    sum += rand
    cnt += 1
sum -= rand
cnt -= 1                   # 카운트 값도 1번 더 증가된 상태이기 때문에 누적값을 한번 빼는 것과 같이 카운트 값도 -1
print("\n누적합 한도가 {}일 때,\n랜덤값 누적합 : {}, 반복 횟수 : {}".format(userin,sum,cnt))
'''

'''(무한 루프 사용)
from random import *
a = int(input("값 입력 : "))
sum = 0
count = 0
while True : 
    randnum = randint(1,10)
    sum += randnum
    count += 1
    if a < sum :
        sum -= randnum
        count -= 1            # 카운트 값도 1번 더 증가된 상태이기 때문에 누적값을 한번 빼는 것과 같이 카운트 값도 -1
        print("총 반복 횟수는 {}이고 누적합은 {}입니다".format(count,sum))
        break
'''

#3.별 찍기 문제
'''
*
**
***
****
*****
출력하기
'''
'''
cnt = 1
while cnt <= 5 :
    print("*"*cnt)
    cnt += 1
'''

'''(무한 루프 사용)
star = 1
while True :
    if star > 5 :
        break
    print("*"*star)
    star += 1
'''

'''(1 ~ 랜덤)
from random import *
cnt = randint(1,10)
num = 1
while num <= cnt :
    print("*"*num)
    num += 1
'''

























