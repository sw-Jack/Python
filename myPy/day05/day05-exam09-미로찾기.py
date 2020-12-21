# 미로찾기 (그림 참고)

def solve_maze(g,start,end) :
    qu = []
    visit = set()   

    qu.append(start)
    visit.add(start)

    while qu :
        p = qu.pop(0)
        v = p[-1]
        if v == end :
            return p
        for x in g[v] :
            if x not in visit :
                qu.append(p+x)
                visit.add(x)
    return "??"
        

    
maze = {
    'a' : ['e'],
    'b' : ['c','f'],
    'c' : ['b','d'],
    'd' : ['c'],
    'e' : ['a','i'],
    'f' : ['b','g','j'],
    'g' : ['f','h'],
    'h' : ['g','l'],
    'i' : ['e','m'],
    'j' : ['f','k','n'],
    'k' : ['j','o'],
    'l' : ['h','p'],
    'm' : ['i','n'],
    'n' : ['m','j'],
    'o' : ['k'],
    'p' : ['l']
    }

print(solve_maze(maze,'a','p'))
