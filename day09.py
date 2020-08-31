print("\n")
# 연습 문제
# 사용자에게 단수를 입력받아서 해당하는 구구단만 출력할 수 있는 프로그램 작성
# 조건
# 사용자는 반드시 2 ~ 9 까지의 숫자만 입력합니다
# 다른 숫자를 입력하면 "잘못된 값입니다. 다시 입력하세요" 라는 문구가 나와야합니다
# 그리고 구구단 출력이 끝나면 다시 단수를 입력받는 문구가 실행이 되어야 합니다
'''
while 1 :
    a = 1
    num = int(input("\n단수 입력 : "))
    if num in range(2,10) :
        while a <= 9 :
            print("{} X {} = {}".format(num,a,num*a))
            a = a + 1
    else :
        print("잘못된 값입니다. 다시 입력하세요")
'''


# break 
# break 를 사용하면 강제적으로 반복문을 빠져나가는 것이 가능합니다
'''
a = 1 
while a == 1 :
    print("a는 %d입니다" %a)
    break                     # 앞 출력문 출력 후 반복문 탈출, 뒷 출력문 출력 X
    print("출력 X")
'''

# break 사용
# 예제
'''
cola = 10
while cola >= 1 :
    print("\n1. 콜라를 준다")
    print("2. 콜라를 주지 않는다")
    print("3. 프로그램을 종료합니다")
    print("4. 콜라 리필")
    user = int(input("원하시는 번호를 입력하세요 : "))
    if user == 1 : 
        print("콜라를 받으세요!")
        cola -= 1
        print("현재 콜라는 %d병 남았습니다" %cola)
    elif user == 2 :
        print("콜라를 주지 않았습니다")
    elif user == 3 :
        print("수고하셨습니다!")
        break
    elif user == 4 :
        print("콜라가 리필되었습니다")
        cola = 10
        print("현재 콜라는 %d병입니다" %cola)
'''


# 연습 문제
# 1 ~ x 까지의 수 중에서 짝수만 출력하는 프로그램
# x 는 사용자가 직접 입력할 수 있도록 합니다
'''
x = int(input("x값 입력 : "))
num = 1
while num <= x :
    if num%2 == 0 :
        print(num, end=' ')
    num += 1
'''

# continue
# continue 를 사용하면 아래 문장을 실행하지 않고 다시 조건식으로 돌아올 수 있습니다
# continue 예제
'''
x = int(input("x값 입력 : "))
num = 0
while num < x :
    num += 1
    if num%2 == 1 :
        continue
    print(num, end=' ')
'''

# 연습 문제
#1. 구구단 전체를 출력하는 프로그램
#조건 : 구구단 출력 시 단을 구별해서 출력
'''
dan = 1
while dan <= 9 :
    print("-"*10);print("{}단".format(dan))
    num = 1
    while num <= 9 :
        print("{} X {} = {}".format(dan,num,dan*num))
        num += 1
    dan += 1
'''

#2. 현재 사용자가 가지고 있는 돈은 10000원입니다
#사용자는 커피를 사려고 하는데 아이스아메리카노는 3000원, 
#카라멜 마끼아또는 4000원,
#캔 커피는 500원입니다
#사용자에게 어떤 것을 마실지 입력을 받아서 구매를 하고 만약 잔액이 부족하다면 "잔액부족" 이라는 문구가 나오도록 만들어주기
#조건 : 사용자가 입력할 때 번호 혹은 커피의 이름으로 입력을 해도 정상적으로 작동할 수 있도록 합니다
#조건 : 커피를 산 후 다시 커피를 살 수 있는 항목이 자동으로 나와야 합니다
#조건 : 사용자가 프로그램을 종료할 수 있어야 합니다
'''
money = 10000
americano = 3000
caramel = 4000
can = 500
while True :
    sum = 0
    while True :   
        tot = 0
        coff = input("커피를 선택\n1.아메리카노\n2.카라멜 마끼아또\n3.캔커피\n4.종료\n주문 : ")
        if coff == 'americano' or coff == '1'  :
            print("\n아메리카노 구매, 가격 : {}\n".format(americano))
            sum += americano
        elif coff == 'caramel' or coff == '2'  :
            print("\n카라멜 마끼아또 구매, 가격 : {}원\n".format(caramel))
            sum += caramel
        elif coff == 'can' or coff == '3'  :
            print("\n캔커피 구매, 가격 : {}\n".format(can))
            sum += can
        elif coff == '4' :
            tot = tot + sum
            break
        else : 
            print("\n메뉴에 없습니다. 다시 입력 하세요\n")
    if tot > money :
        print("주문 총액 : {}원, 잔액 부족!\n".format(sum))
    else :
        print("주문 총액 : {}원\n".format(sum))
        break
'''


#3. 1 ~ 100 까지의 누적합을 구하는 프로그램
'''
sum = 0
while st <= 100 :
    sum += st
    st += 1
print(sum)
'''
