import sys
import heapq
from collections import deque
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
def find(a, b) :
    if uf[a][b] == -1 : return (a, b)
    uf[a][b] = find(uf[a][b])
    return uf[a][b]

def union(a, b, c, d) :
    a = find(a, b)
    b = find(c, d)
    if a == b : return
    uf[a[0]][a[1]] += uf[b[0]][b[1]]
    uf[b[0]][b[1]] = (a[0], a[1])

#N = int(input())
N, K = map(int,input().split())

uf = [[(-1, -1)]*(N+1) for i in range (N+1)]
move = [[-1,0], [1,0], [0,-1], [0,1]]


dq = deque() # BFS 용 lst
for i in range (K) :
    a, b = map(int, input().split())
    uf[a][b] = 0
    dq.append((a,b))

for i in range (1, N+1) :
    for j in range (1, N+1) :
        for _, __ in move : 
            dx = j + _
            dy = i + __
            if 0 < dx <= N and 0 < dy <= N :
                if uf[i][j] == uf[dy][dx] == 0 :
                    union(i, j, dx, dy)

cnt = 0
while dq : 
    for i in range (len(dq)) : 
        y, x = dq.popleft()
        for _, __ in move :
            dx = x + _
            dy = y + __
            if 0 < dx <= N and 0 < dy <= N :
                union(x, y, dx, dy)
    cnt += 1
