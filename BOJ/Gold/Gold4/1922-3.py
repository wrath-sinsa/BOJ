import sys
import heapq
import math
from collections import deque
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

N = int(input())
#N, M = map(int,input().split())
M = int(input())

graph = [list() for i in range (N+1)]

for i in range (M) :
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

for i in range (1, N+1) :
    heapq.heapify(graph[i])

INF = 1000 * 10000
used = [0] * (N+1)

lst = list()
push(lst, (0,1))

ans = 0
for i in range (1, N+1):
    now = -1
    min_dist = INF
    while (lst):
        now = lst[0][1]
        if (used[now] == 0) :
            ans += lst[0][0]
            break
        pop(lst)
    used[now] = 1
    for exp, nxt in graph[now] :
        push(lst, (exp,nxt))
print(ans)
