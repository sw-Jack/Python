import random

a = random.randint(1,100)
b = random.randint(1,100)

print(a, '+', b, '=')
x = input()

res = int(x)

if a + b == res :
    print("정답입니다")
else :
    print("머징?")
