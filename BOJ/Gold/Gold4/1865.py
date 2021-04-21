import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

T = int(input())
#N, M = map(int,input().split())
for i in range (T) :
    N, M, W = map(int, input().split())

    graph = [list() for i in range (N+1)]
    for i in range (M) :
        S, E, T = map(int, input().split())
        graph[S].append((E, T))
        graph[E].append((S, T))

    for i in range (W) :
        S, E, T = map(int, input().split())
        graph[S].append((E, -T))

    MAX = 5000001
    # MIN = N * N * -C
    dis = [MAX] * (N+1) 

    cycle = 0
    for i in range (1, N+1) :
        for j in range (1, N+1) :
            for nxt, cost in graph[j] :
                if dis[nxt] > dis[j] + cost :
                    dis[nxt] = dis[j] + cost
                    if i == N :
                        cycle = 1

    if cycle : print("YES")
    else :print("NO")