import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
def find(n) :
    if uf[n] < 0 : return n
    uf[n] = find(uf[n])
    return uf[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a == b : return False
    uf[a] += uf[b]
    uf[b] = a

T = int(input())
for i in range (T) :
    N, M = map(int,input().split())
    
    dot = list()
    for j in range (M) :
        a, b = map(int, input().split())
        dot.append((a,b))

    graph = [[0] * N for i in range (N)]
    for i in range (N) :
        x1, y1 = dot[i][0], dot[i][1]
        for j in range (N) : 
            x2, y2 = dot[j][0], dot[j][1]
            graph[i][j] = math.sqrt((x2-x1)**2+(y2-y1)**2)

    used = [0] * (N)
    lst = list()
    push(lst, (0, 0))

    ans = 0
    for i in range (N) :
        print(lst)
        now = -1
        while lst :
            z, y = pop(lst)
            if used[y] == 0 :
                ans = z
                now = y
                break

        used[now] = 1
        for nxt, exp in enumerate (graph[now]) :
            push(lst, (exp, nxt))
    print(ans)