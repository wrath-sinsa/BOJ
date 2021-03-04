import sys
import heapq
input = sys.stdin.readline

N, E = map(int, input().split())

lst = [list() for i in range (N+1)]
for i in range(E) :
    tmp = list(map(int, input().split()))
    lst[tmp[0]].append((tmp[2], tmp[1]))

v, w = map(int, input().split())
to_vw = [0,0,0,0]

hq = list()

def Dijkstra(a) :
    heapq.heappush(hq, (0, a))
    cost_lst = [sys.maxsize] * (N+1)
    cost_lst[a] = 0
    while hq :
        expense, now = heapq.heappop(hq)
        if cost_lst[now] < expense : continue
        for cost, nxt in lst[now] :
            nxt_cost = cost + expense
            if nxt_cost < cost_lst[nxt] :
                cost_lst[nxt] = nxt_cost
                heapq.heappush(hq, (nxt_cost, nxt))
    
Dijkstra(1)
Dijkstra(v)
Dijkstra(w)