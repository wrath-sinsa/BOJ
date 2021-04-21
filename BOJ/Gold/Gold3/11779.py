import sys
import heapq
from collections import deque
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def Dijkstra(a, b) :
    cost = [sys.maxsize] * (N+1)
    cost[a] = 0
    lst = list() # heapq
    seq = [0] *(N+1) # 방문 순서
    push(lst, (0, a))
    while lst :
        time, now = pop(lst)
        if time > cost[now] : continue   

        for nxt, exp in graph[now] :                      
            nxt_cost = time + exp
            if cost[nxt] > nxt_cost :
                seq[nxt] = now # 방문 순서
                cost[nxt] = nxt_cost
                push(lst, (nxt_cost, nxt))
    #print(cost)
    print(cost[b])
    #print(seq)
    ans = list()
    while b != a :
        ans.append(b)
        b = seq[b]
    ans.append(a)
    print(len(ans))
    for i in reversed(ans) :
        print(i, end = " ")
# __main__

N = int(input())
#N, M = map(int,input().split())
M = int(input())

graph = [list() for i in range (N+1)]
for i in range (M) :
    a, b, c = map(int, input().split())
    graph[a].append((b,c))
u, v = map(int, input().split())

Dijkstra(u, v)
