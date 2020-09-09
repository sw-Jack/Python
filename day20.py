# 연습 문제 : 컴퓨터와 가위바위보 게임
# 5판 3선승으로 진행합니다
# 한 판 진행할 때마다 결과가 출력이 되어야 합니다
# 가위바위보가 끝나면 승,패,무 결과가 출력되면서 계속 할 것인지 물어봐야 합니다
# 출력 양식 -> 승 : 1, 패 : 1, 무 : 1
'''
from random import *
while True : 
    win = draw = lose = 0    # 전적을 누적할 승, 무, 패 변수 생성 및 초기화
    while True :
        user = input("\n<가위바위보 게임>\n가위 바위 보 중 선택하세요 : ")  # 사용자 입력
        com = randint(1,3)   # 컴퓨터가 낼 가위,바위,보를 랜덤값으로 생성, 그 생성한 랜덤값을 받을 변수 com
        if com == 1 :   # 랜덤값이 1이 나오면 com은 1
            com = '가위'
            print("*컴퓨터 : {}".format(com))
        elif com == 2 :   # 랜덤값이 2가 나오면 com은 2
            com = '바위'
            print("*컴퓨터 : {}".format(com))
        else :           # 랜덤값이 3이 나오면 com은 3
            com = '보'
            print("*컴퓨터 : {}".format(com))
        if user == com :    # 무승부 경우, 사용자 입력과 컴퓨터가 낸 것이 같으면 무승부
            draw += 1   # 무 전적 +1(누적)
            print('*결과 : 무')
        elif user == '가위' :   # 사용자가 가위를 낸 경우
            if com == '보' :    # 컴퓨터가 보를 내면 승
                win += 1    # 승 전적 +1(누적)
                print('*결과 : 승')
            else :  #  컴퓨터가 바위를 낸 경우
                lose += 1   # 패 전적 +1(누적)
                print('*결과 : 패')      
        elif user == '바위' :   # 사용자가 바위를 낸 경우
            if com == '가위' :   # 컴퓨터가 가위를 내면 승
                win += 1    # 승 전적 +1(누적)
                print('*결과 : 승')
            else :   # 컴퓨터가 보를 내면 패
                lose += 1   # 패 전적 +1(누적)
                print('*결과 : 패')
        elif user == '보' :    # 사용자가 보를 낸 경우
            if com == '바위' :  # 컴퓨터가 바위를 내면 승
                win += 1    # 승 전적 +1(누적)
                print('*결과 : 승')
            else :    # 컴퓨터가 가위를 내면 패
                lose += 1   # 패 전적 +1(누적)
                print('*결과 : 패')
        if win == 3 :   # 5판 3선승제이므로 5판을 다하지 않았는데 이미 3승이 이루어지는 경우 결과를 출력하고 반복문 break
            print("\n<결과>\n승\n<총 전적>\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            break
        elif win+draw+lose == 5 :   # 5판전이므로 승, 무, 패 합이 5가 되는 경우
            if win > lose :   # 승이 패보다 많으면 승, 결과 출력 반복문 break
                print("\n<결과>\n승\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            elif win == lose :  # 승과 패가 같으면 무승부, 결과 출력 반복문 break
                print("\n<결과>\n무\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            else :   # 패가 승보다 많으면 패, 결과 출력 반복문 break
                print("\n<결과>\n패\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            break
    q = input("다시 하시겠습니까 (y/n) : ") # 가위바위보 종료 후 다시 하겠냐는 문구 출력
    if q == 'y' :  # y를 입력하ㅏ면 다시 처음으로 돌아가 프로그램 반복 continue
        continue
    else :  # y 이외의 것을 입력하면 바로 프로그램 종료
        print('프로그램 종료')
        break
'''

'''(case2 함수 사용)
def computer() :   # 컴퓨터가 낼 가위바위보 랜덤값을 변수에 저장해주는 함수
    global com
    if com == 1 :
        com = '가위'
    elif com == 2 :
        com = '바위'
    else :
        com = '보'
def dr(u,c) :    # 무승부 함수
    global draw
    if u == c :        
        draw += 1
        print('*결과 : 무')
def wi(u,c) :    # 승리 함수
    global win
    if u == '가위' :
        if c == '보' :
            win += 1
            print('*결과 : 승')
    elif u == '바위' :
        if c == '가위' :
            win += 1
            print('*결과 : 승')
    elif u == '보' :
        if c == '바위' :
            win += 1
            print('*결과 : 승')
def los(u,c) :   # 패배 함수
    global lose
    if u == '가위' :
        if c == '바위' :
            lose += 1
            print('*결과 : 패')  
    elif u == '바위' :
        if c == '보' :
            lose += 1
            print('*결과 : 패')  
    elif u == '보' :
        if c == '가위' :
            lose += 1
            print('*결과 : 패')                  
from random import *
while True : 
    win = draw = lose = 0
    while True :
        user = input("\n<가위바위보 게임>\n가위 바위 보 중 선택하세요 : ")
        com = randint(1,3)
        computer()   # 함수 호출
        print("*컴퓨터 : {}".format(com))
        dr(user,com)   # 함수 호출
        wi(user,com)   # 함수 호출
        los(user,com)  # 함수 호출
        if win == 3 :
            print("\n<결과>\n승\n<총 전적>\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            break
        elif lose == 3 :
            print("\n<결과>\n패\n<총 전적>\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            break
        elif win+draw+lose == 5 :
            if win > lose :
                print("\n<결과>\n승!\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            elif win == lose :
                print("\n<결과>\n무!\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            else :
                print("\n<결과>\n패!\n[총 전적]\n승 : {}, 무 : {}, 패 : {}".format(win,draw,lose))
            break
    q = input("다시 하시겠습니까 (y/n) : ")
    if q == 'y' :
        continue
    else : 
        break
'''


'''
승, 패, 무 = 0, 0, 0
def win() :
    global 승
    print('플레이어 승')
    승 = 승 + 1
    if 승 == 3 :
        system('cls')
        print("플레이어 승리!")
        print("총 전적 : 승:{} 패:{} 무:{}".format(승, 패, 무))
def lose() :
    global 패
    print('플레이어 패')
    패 = 패 + 1
    if 패 == 3 :
        system('cls')
        print("플레이어 패배......")
        print("총 전적 : 승:{} 패:{} 무:{}".format(승, 패, 무))
def draw():
    global 무
    무 = 무 + 1
    print("무승부!")
def result():
    if 승 == 패 :
        system("cls")
        print("무승부 입니다!")
        print("총 전적 : 승:{} 패:{} 무:{}".format(승, 패, 무))
    elif 승 == 1 and 승 > 패 :
        system("cls")
        print("플레이어의 승리 입니다!")
        print("총 전적 : 승:{} 패:{} 무:{}".format(승, 패, 무))
    elif 승 == 1 and 승 < 패 :
        system("cls")
        print("플레이어의 패배 입니다....")
        print("총 전적 : 승:{} 패:{} 무:{}".format(승, 패, 무))
    elif 승 == 0 and 승 < 패:
        system("cls")
        print("플레이어의 패배 입니다....")
        print("총 전적 : 승:{} 패:{} 무:{}".format(승, 패, 무))
    elif 승 == 2 :
        system("cls")
        print("플레이어의 승리 입니다!")
        print("총 전적 : 승:{} 패:{} 무:{}".format(승, 패, 무))
from os import system
from random import *
while True:
    승,패,무 = 0,0,0
    for x in range(5):
        player = input('가위, 바위, 보 : ')
        computer = randint(0,2) # 0 = 가위 ,  1 = 주먹 ,2= 보
        if player == '가위':
            if computer == 0:
                draw()
            elif computer == 1:
                lose()
                if 패 == 3 :
                    break
            elif computer == 2:
                win()
                if 승 == 3 :
                    break
        elif player == '바위':
            if computer == 0:
                win()
                if 승 == 3 :
                    break
            elif computer == 1:
                draw()
            elif computer == 2:
                lose()
                if 패 == 3 :
                    break
        elif player == '보':
            if computer == 0:
                lose()
                if 패 == 3 :
                    break
            elif computer == 1:
                win()
                if 승 == 3 :
                    break
            elif computer == 2:
                draw()
    result()     
    retry = input('계속 진행 하시겠습니까?(Yes/No) : ')
    if retry  == 'No':
        print("수고하셨습니다")
        break
'''



# 클래스 (class)
# 클래스란 함수와 변수들의 집합체를 의미한다.
# 클래스 안에는 인스턴스(객체)를 만들어서 사용할 수 있습니다
# class의 선언은 일반 함수 선언과 유사합니다
# class를 선언할 때는 def가 아닌 class를 적어야합니다
# 그리고 class 이름의 첫글자는 대문자로 표시합니다
'''
class Ham :      # 햄버거 클래스 생성
    def recipe(self,a,b) :   # 클래스 안에 있는 함수를 메소드라 지정합니다  # self : 객체가 들어올 자리
        print("%s버거는 %s와 %s로 만들어집니다" %(a,a,b))

Ham1 = Ham()   # Ham1 이라는 객체를 생성
Ham1.recipe('치즈','양상추')
Ham2 = Ham()   # Ham1 과 다른 Ham2 라는 객체 생성
Ham2.recipe('치킨','토마토')
'''

# 계산기의 기능 중 + 기능만 가능한 프로그램
# 함수만 사용하면 기본적으로 2개의 계산기를 정상적으로 사용할 수 없습니다
# 그래서 메소드에서 첫번째로 정의되어 있는 매개변수에는 객체가 들어가는 매개변수로 사용합니다
# 클래스를 사용하면 객체 단위로 프로그래밍을 할 수 있습니다
# 그냥 함수로 사용하는 것도 가능하지만 클래스를 사용하면 좀 더 효율적인 코딩이 가능합니다
'''
while True :
    sum = 0  # 아래의 break를 통해 반복문을 빠져나오면 누적합 0으로 초기화
    while True :
        n = int(input('\n더할 정수 입력 (나가기 0): '))
        sum += n  # 입력한 더할 정수는 누적합이 적용
        if n == 0 :  # 더 이상 계산하지 않으려면 0을 입력
            break  # 반복문 탈출
        print('{}'.format(sum))  # 현재까지의 누적합 출력
'''


'''(함수 사용) -> 2개 계산기 사용 X
sum = 0  # 누적합 0으로 초기화
def add(num) :  # 덧셈 연산 함수, 사용자 입력값의 인수를 매개변수 num에 저장
    global sum   # 전역 변수 sum
    sum += num   # 누적합
    return sum   # 누적합 반환
while True : 
    a = int(input("\n<첫번째 계산기>\n더할 정수 입력 (나가기 0) : "))
    print(add(a))  # 덧셈 연산 함수 호출
    if a == 0 : # 0을 입력하면 계산기 종료
        break  # (첫번째 계산기의) 반복문이 끝나면 바로 두번째 계산기 실행
while True :  # 여기서의 문제점 : 앞선 첫번째 계산기에서의 덧셈 연산이 누적된 값으로 남아있음
            # 따라서 두번째 계산기의 첫 연산 실행 시, 이전의 연산 누적값이 계속 이어져 더해짐
    b = int(input("\n<두번째 계산기>더할 정수 입력 (나가기 0) : "))
    print(add(b))
    if b == 0 :
        break
'''

'''
class Calc :
    sum = 0
    def _init_(self) :  # 매개변수 X, 오직 객체 매개변수만
        self.sum = 0
    def add(self,a) :  # 사용자가 입력하는 값의 인수를 받을 매개변수 1개, 나머진 객체 매개변수
        self.sum = self.sum + a
        return self.sum
calc1 = Calc()   # Calc 클래스를 받을 calc1 객체 생성 : 첫번째 계산기
calc2 = Calc()   # Calc 클래스를 받을 calc2 객체 생성 : 두번쨰 계산기
while True :
    calc1._init_()    # 첫번째 계산기 초기화 메소드 호출(첫번째 계산기 실행 종료시)
    calc2._init_()    # 두번째 계산기 초기화 메소드 호출(두번째 계산기 실행 종료시)
    # 사용할 계산기 선택하도록 만듦
    c = int(input('\n# 사용할 계산기 선택 (프로그램 종료 0): '))
    if c == 1 : # 사용자 입력값이 1이면 첫번째 계산기 실행
        while True : 
            a = int(input("\n[첫번째 계산기]\n더할 정수 입력 (나가기 0) : "))
            print(calc1.add(a))  # calc1 객체 사용해서 클래스의 덧셈 메소드 호출
            if a == 0 :  # 0 입력시 첫번째 계산기 사용 종료(계산기 선택창으로)
                break
    elif c == 2 : # 사용자 입력값이 2이면 두번째 계산기 실행
        while True :
            b = int(input("\n[두번째 계산기]\n더할 정수 입력 (나가기 0) : "))
            print(calc2.add(b))  # calc2 객체 사용해서 클래스의 덧셈 메소드 호출
            if b == 0 :  # 0 입력시 두번째 계산기 사용 종료(계산기 선택창으로)
                break
    elif c == 0 :
        print("프로그램 종료")
        break
'''

























