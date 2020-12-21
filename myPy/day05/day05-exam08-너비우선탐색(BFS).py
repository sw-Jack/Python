# 너비 우선 탐색 (BFS)
# v1
def bfs1(graph, start) :
    visit = []
    qu = []

    qu.append(start)

    while qu :
        node = qu.pop(0)
        if node not in visit :
            visit.append(node)
            qu.extend(graph[node])
    return visit

# v2
def bfs2(graph, start) :
    qu = []
    done = set()

    qu.append(start)
    done.add(start)

    while qu :
        p = qu.pop(0)
        print(p)
        for x in graph[p] :
            if x not in done :
                qu.append(x)
                done.add(x)
    return done


g = {
    1 : [2,3],
    2 : [1,4,5],
    3 : [1],
    4 : [2],
    5 : [2]
    }

print(bfs1(g,1))
print()
print(bfs2(g,1))

