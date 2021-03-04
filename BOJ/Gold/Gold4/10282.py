import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def Dijkstra(a):
    cost_lst = [sys.maxsize] * (N+1)
    hq = list()
    cost_lst[a] = 0
    push(hq, (0, a))
    while hq :
        exp, now = pop(hq)
        if cost_lst[now] < exp : continue
        for nxt, cost in lst[now] :
            nxt_cost = exp + cost
            if nxt_cost < cost_lst[nxt] :
                cost_lst[nxt] = nxt_cost
                push(hq, (nxt_cost, nxt))
    cost_lst = [i for i in cost_lst if i != sys.maxsize]
    print(len(cost_lst), max(cost_lst)) 

# __main__
T = int(input())
for i in range (T) :
    N, M, X = map(int, input().split())
    lst = [[] for i in range (N+1)]
    for i in range (M) :
        tmp = list(map(int, input().split()))
        lst[tmp[1]].append((tmp[0], tmp[2]))
    #print(lst)
    Dijkstra(X)