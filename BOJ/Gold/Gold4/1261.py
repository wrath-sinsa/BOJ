import sys
import heapq
input = sys.stdin.readline

M, N = map(int,input().split())

lst = []
for i in range(N):
    tmp = list(map(int,input().rstrip()))
    lst.append(tmp)

#print(lst)

# used 확장
cost_lst = [[sys.maxsize]*M for i in range (N)]

# hq
hq = list()

# move
move = [[0, -1], [0, 1], [1, 0], [-1, 0]]

def Dijkstra() :
    heapq.heappush(hq, (0, 0, 0))
    cost_lst[0][0] = 0

    while hq :
        y, x, exp = heapq.heappop(hq)

        if cost_lst[y][x] < exp : continue

        for dy, dx in move :
            tmp_y = y + dy
            tmp_x = x + dx
            if 0 <= tmp_y < N and 0 <= tmp_x < M :
                nxt_cost = exp + lst[tmp_y][tmp_x]
                if nxt_cost < cost_lst[tmp_y][tmp_x] :
                    cost_lst[tmp_y][tmp_x] = nxt_cost
                    heapq.heappush(hq, (tmp_y, tmp_x, nxt_cost))

Dijkstra()
print(cost_lst[N-1][M-1])