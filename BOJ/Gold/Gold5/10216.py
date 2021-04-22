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

def union(a, b) :
    a = find(a)
    b = find(b)
    if a == b : return False
    uf[a] += uf[b]
    uf[b] = a
    return True
T= int(input())
for i in range (T) :
    
    N= int(input())
    #N, M = map(int,input().split())
    graph = list()
    for j in range (N):
        x,y,r= map(int, input().split())
        graph.append((x,y,r))
    #print(graph)

    uf = [-1] * (N)

    for i in range (N) :
        x1, y1, r1 = graph[i][0], graph[i][1], graph[i][2]
        for j in range (N) :
            x2, y2,r2 = graph[j][0], graph[j][1], graph[j][2]
            dis = math.sqrt((x2-x1)**2+(y2-y1)**2)
            if dis <= r1 + r2 :
                union(i, j)

    #print(uf)
    ans = 0
    for i in range (N) :
        if uf[i] < 0 :
            ans += 1
    print(ans)