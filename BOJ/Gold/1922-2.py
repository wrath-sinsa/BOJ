import sys
import heapq
import math
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
    a, b, c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

INF = 1000*10000
dist = [INF] * (N+1)
used = [0] * (N+1)
dist[1] = 0

ans = 0
for i in range (1, N+1) : # N 번 반복?
    now = -1
    min_dist = INF
    for j in range (1, N+1) :
        if used[j] == 0 and min_dist > dist[j] : # 최소 간선을 찾음 O(N)
            min_dist = dist[j]
            now = j
    if now < 0 : print("연결 안됨")
    ans += min_dist
    used[now] = 1
    for nxt, exp in graph[now] : # 갱신
        dist[nxt] = min(dist[nxt], exp)
print(ans)

## MST에 있어 prim 알고리즘 O(N^2)