import sys
import heapq

V, E = map(int, sys.stdin.readline().split())

K = int(sys.stdin.readline())

nod_lst = [[] for i in range (V+1)]

for i in range (E) :
    u, v, w = map(int, sys.stdin.readline().split())
    nod_lst[u].append([v, w])


# 이동 초기화 최대치 설정
maximum = sys.maxsize

# 이동 시간 저장 리스트
cost_lst = [maximum] * (V+1)
cost_lst[K] = 0

# 실행을 위한 우선순위 큐
lst = []
heapq.heappush(lst, [0, K])

def Dijkstra() :
    while lst :
        where = heapq.heappop(lst)
        now = where[1]
        expence = where[0]
        if cost_lst[now] < expence : # 이미 들어가있는 요소 중 제거
            continue
        for nxt, cost in nod_lst[now] :
            nxt_cost = cost + cost_lst[now]
            if nxt_cost < cost_lst[nxt] :
                cost_lst[nxt] = nxt_cost
                heapq.heappush(lst, [cost_lst[nxt], nxt])

Dijkstra()

for i in range (1, V+1) :
    if cost_lst[i] != maximum :
        print(cost_lst[i])
    else :
        print("INF")