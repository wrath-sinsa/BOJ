import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())

lst = [list() for i in range (N+1)]
for i in range (M) :
    tmp = list(map(int, input().split()))
    lst[tmp[0]].append((tmp[1], tmp[2]))

#print(lst)

# hq
hq = list()

# ans_lst
A = [0] * (N+1)
B = [0] * (N+1)

def Dijkstra(a) :
    cost_lst = [sys.maxsize] * (N+1)
    cost_lst[a] = 0

    heapq.heappush(hq, (0, a))
    while hq :
        exp, now = heapq.heappop(hq)
        if cost_lst[now] < exp : continue
        for nxt, cost in lst[now] :
            nxt_cost = cost_lst[now] + cost
            if nxt_cost < cost_lst[nxt] :
                cost_lst[nxt] = nxt_cost
                heapq.heappush(hq, (nxt_cost, nxt))
    A[a] = cost_lst[X]
    if a == X :
        for i in range (1, N+1) :
            B[i] = cost_lst[i]

for i in range (1, N+1) :
    Dijkstra(i)
#print(A)
#print(B)
ans = [i+j for i, j in zip(A, B)]
print(max(ans))
