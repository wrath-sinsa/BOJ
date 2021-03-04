import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def Dijkstra(a):
    cost_lst = [sys.maxsize] * (N +1 )
    hq = list()
    cost_lst[a] = 0
    push(hq, (0, a))
    ans = list()
    while hq :
        exp, now = pop(hq)
        if cost_lst[now] < exp : continue
        ans.append(now)
        for nxt, cost in lst[now] :
            nxt_cost = exp + cost
            if nxt_cost < cost_lst[nxt] :
                cost_lst[nxt] = nxt_cost
                push(hq, (nxt_cost, nxt))
    print(cost_lst[b])
    print(len(ans))
    print(i for i in ans)
    print(ans)

# __main__
N = int(input())
M = int(input())
lst = [[] for i in range (N+1)]
for i in range (M) :
    tmp = list(map(int, input().split()))
    lst[tmp[0]].append((tmp[1], tmp[2]))
#print(lst)
a, b = map(int, input().split())
Dijkstra(a)