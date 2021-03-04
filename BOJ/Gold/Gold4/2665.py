import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def Dijkstra():
    cost_lst = [[sys.maxsize] * N for i in range (N)]
    hq = list()
    cost_lst[0][0] = 0
    push(hq, (0, 0, 0))
    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while hq :
        exp, y, x = pop(hq)
        if cost_lst[y][x] < exp : continue
        for dy, dx in d :
            tmp_y = y + dy
            tmp_x = x + dx
            if 0 <= tmp_y < N and 0 <= tmp_x < N :
                nxt_cost = exp
                if lst[tmp_y][tmp_x] == 0 : nxt_cost += 1
                if nxt_cost < cost_lst[tmp_y][tmp_x] :
                    cost_lst[tmp_y][tmp_x] = nxt_cost
                    push(hq, (nxt_cost, tmp_y, tmp_x))
    print(cost_lst[N-1][N-1])

# __main__
N = int(input())
lst = []
for i in range (N) :
    tmp = list(map(int, list(input().rstrip())))
    lst.append(tmp)
#print(lst)
Dijkstra()