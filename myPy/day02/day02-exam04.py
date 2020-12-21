import time

input("엔터를 누르고 30초를 셉니다.")
start = time.time()

input("30초 후에 다시 엔터를 누르세오.")
end = time.time()

res = end - start
print("실제 시간 : ", res, "초")
print("차이 : ", abs(res-30), "초")

 
