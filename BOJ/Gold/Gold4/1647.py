import sys
import heapq
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
    a,b,c= map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = 1000 * 100000

used = [0] * (N+1)
lst = list()
push(lst, (0,1))

ans = 0
max_dist = 0
for i in range (1, N+1) :
    now = -1
    while lst :
        z, y = pop(lst) # M * log
        if used[y] == 0 :
            now = y
            ans += z
            if z > max_dist : max_dist = z
            break
    used[now] = 1
    for nxt, exp in graph[now] : # M
        push(lst, (exp, nxt)) # log
print(ans-max_dist)
#prim O(MlogN) 약 1000,000 * 16
#Kruskal O(MlogM) 약 1000,000 * 20
