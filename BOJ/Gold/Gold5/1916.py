import sys
import heapq
input = sys.stdin.readline

N = int(input())
M = int(input())

lst = [list() for i in range (N+1)]
for i in range (M) :
    tmp = list(map(int, input().split()))
    lst[tmp[0]].append((tmp[1], tmp[2]))

A, B = map(int, input().split())

maximum = sys.maxsize
cost_lst = [maximum] * (N+1)
cost_lst[A] = 0

hq = list()

def Dijkstra() :
    heapq.heappush(hq, (0, A))
    while hq :
        expense, now = heapq.heappop(hq)
        if cost_lst[now] < expense : continue # 비싼곳에서 왔을때 볼필요없음.
        for nxt, cost in lst[now] :
            nxt_cost = cost_lst[now] + cost
            if nxt_cost < cost_lst[nxt] : # 왔는데 더 쌀 경우
                cost_lst[nxt] = nxt_cost
                heapq.heappush(hq, (nxt_cost, nxt))

Dijkstra()
#print(cost_lst)
print(cost_lst[B])