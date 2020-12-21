# 회문 찾기
# - 회문 : 거꾸로 해도 같은 단어나 문장
# ex) 기러기, 일요일, 사진사, 다가가다 / mom, wow, level, noon
# 큐(Queue)나 스택(Stack) 활용 
# 큐 -> FIFO (First In First Out) : enque / deque
# 스택 -> LIFO (Last In First Out) : push / pop

# 코드

def palindrome(s) :
    qu = []
    st = []

    for x in s :
        if x.isalpha() :
            qu.append(x.lower())
            st.append(x.lower())

    while qu :
        if qu.pop(0) != st.pop() :
            return False
    return True

    
print(palindrome("Wow"))
print(palindrome("Wkate"))
print(palindrome("Madam,I am Adam"))
print()



# Quiz : 큐와 스택을 이용하지 않고 그냥 글자의 앞과 뒤를 비교해
# 회문인지 판별

# 코드
def palidrome2(s) :
    leng = len(s)
    mid = leng // 2

    for i in range(mid) :
        if s[i].lower() != s[leng-1-i].lower() :
            return False
    return True

print(palidrome2("memory"))
print(palidrome2("Wow"))
print(palidrome2("Wkate"))
print(palidrome2("Madam,I am Adam"))
    









































