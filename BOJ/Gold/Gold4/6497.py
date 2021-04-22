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
#N = int(input())

N, M = map(int,input().split())
while (N != 0 and M != 0) :
    graph = [list() for i in range (N+1)]
    uf = [-1] * (N+1)
    hq = list()
    for i in range (M) :
        x, y, z = map(int, input().split())
        graph[x+1].append((y+1, z))
        graph[y+1].append((x+1, z))
        push(hq, (z, x, y))

    cnt = 0
    ans = 0
    #print(hq)
    while cnt != N-1 :
        z, x, y = pop(hq)
        if (union(x, y) == False) :
            ans += z
        else : cnt += 1
    while hq :
        z, x, y = pop(hq)
        ans += z
    print(ans)
    N, M = map(int,input().split())