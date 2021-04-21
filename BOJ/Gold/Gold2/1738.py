import sys
import heapq
from collections import deque
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
#N = int(input())
N, M = map(int,input().split())

graph = [list() for i in range (N+1)]
for i in range (M) :
    u, v, w = map(int,input().split())
    graph[u].append((v,w))

## BFS
lst = deque()
lst.append(1)
used = [0] * (N+1)
used[1] = 1

while lst :
    now = lst.popleft()
    used[now] = 1
    for nxt, exp in graph[now] :
        if used[nxt] == 0 :
            used[nxt] = 1
            lst.append(nxt)
#print(used)
##

MIN = -1000*100-1

dist = [MIN] * (N+1)
dist[1] = 0

move = [0] * (N+1)
cycle = 0

for i in range (1,N+1) :
    for j in range (1,N+1) :
        if dist[j] == MIN : continue
        for nxt, exp in graph[j] :
            nxt_cost = dist[j] + exp
            if dist[nxt] < nxt_cost :
                move[nxt] = j
                dist[nxt] = nxt_cost
                if i == N and used[j] == 1 :
                    cycle = 1


if used[N] == 0 : print(-1)
elif cycle : print(-1)
else : 
    ans = list()
    while N != 1 :
        ans.append(N)
        N = move[N]
    ans.append(1)
    print(*ans[::-1])