# 친구의 친구 찾기 : 그래프
# summer - john
# summer - justine
# summer - mike

# justine - may

# may - kim

# john - justine

# justine - mike

# tom - jerry

fr_info = {
    'summer' : ['john','justine','mike'],
    'john' : ['summer','justine'],
    'justine' : ['john','summer','mike','may'],
    'mike' : ['summer','justine'],
    'may' : ['justine','kim'],
    'kim' :['may'],
    'tom' : ['jerry'],
    'jerry' :['tom']
    }

# 알고리즘
# (1) 앞으로 처리할 사람들을 임시로 저장할 큐를 만든다.
# (2) 이미 큐에 추가한 사람들을 저장할 집합(done)을 만든다.
# (3) 검색의 출발점이 될 사람을 큐와 집합에 추가한다.
# (4) 큐에 사람이 남아 있다면 큐에서 처리할 사람을 꺼낸다.
# (5) 꺼낸 사람을 출력한다.
# (6) 꺼낸 사람의 친구들 중 아직 큐에 추가된 적이 없는 사람을 골라
# 큐와 집합에 추가한다.
# (7) 큐에 처리할 사람이 남아 있으면 4번부터 반복한다. 

# 코드
def print_all_friends(g, start) :
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu :
        p = qu.pop(0)
        print(p)
        for x in g[p] :
            if x not in done :
                qu.append(x)
                done.add(x)

print_all_friends(fr_info, 'summer')
print()
print_all_friends(fr_info, 'jerry')



# Quiz : 친밀도 추가 출력
def print_all_friends(g, start) :
    qu = []
    done = set()

    qu.append((start, 0))
    done.add(start)

    while qu :
        (p, d) = qu.pop(0)
        print(p,d)
        for x in g[p] :
            if x not in done :
                qu.append((x,d+1))
                done.add(x)
                
print_all_friends(fr_info, 'summer')
print()
print_all_friends(fr_info, 'jerry')
































