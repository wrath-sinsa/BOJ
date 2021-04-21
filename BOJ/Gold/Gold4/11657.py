import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))
MAX = 5000001
# __main__
#N = int(input())
N, M = map(int,input().split())
graph = [list() for i in range (N+1)]
dis = [MAX] *  (N+1) 
for i in range (M) :
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append((tmp[1], tmp[2]))

dis[1] = 0
cycle = False
for i in range (N) : # (N-1) + 1 번만큼
    for j in range (1, N+1) : # 1번 도시에서 출발하면서
        if dis[j] == MAX : continue
        for nxt, cost in graph[j] : 
            if dis[nxt] > dis[j] + cost :
                dis[nxt] = dis[j] + cost
                if i == N - 1 :
                    cycle = True

if cycle : print (-1)
else :
    for i in range (2, N+1) :
        if dis[i] == MAX : print("-1")
        else : print(dis[i])