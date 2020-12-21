# 함수의 그래프를 그리는 프로그램
import turtle as t

# 그래프를 그릴 x좌표의 범위
x_min = -5
x_max= 5

# 그래프를 그릴 y좌표의 범위
y_min = -5
y_max = 5

# 그래프를 그릴 간격
space = 0.1


# 그릴 함수 목록
func_list = ["y = x*x", "y = abs(x)", "y = 0.5 * x + 1"]

# 좌표 설정, 거북이 속도, 선 굵기
t.setworldcoordinates(x_min, y_min, x_max, y_max)
t.speed(0)
t.pensize(2)

# x축 그리기
t.up()
t.goto(x_min, 0)
t.down()
t.goto(x_max, 0)

# y축 그리기
t.up()
t.goto(0, y_min)
t.down()
t.goto(0, y_max)

# 그래프 그리기
t.color("green")
for func in func_list :
    x = x_min
    exec(func)  # 문자열의 수식을 실제 수식으로 인식해 실행하는 함수
    t.up()
    t.goto(x,y)
    t.down()
    while x <= x_max :
        x = x + space
        exec(func)
        t.goto(x,y)






















    
