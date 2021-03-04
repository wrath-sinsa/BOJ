import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def Dijkstra(a):
    cost_lst = [[sys.maxsize] * N for i in range (N)]
    hq = list()
    cost_lst[0][0] = lst[0][0]
    push(hq, (lst[0][0], 0, 0))
    d = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    while hq :
        exp, y, x = pop(hq)
        if cost_lst[y][x] < exp : continue
        for dy, dx in d :
            tmp_y = y + dy
            tmp_x = x + dx
            if 0 <= tmp_y < N and 0 <= tmp_x < N :
                nxt_cost = exp + lst[tmp_y][tmp_x]
                if nxt_cost < cost_lst[tmp_y][tmp_x] :
                    cost_lst[tmp_y][tmp_x] = nxt_cost
                    push(hq, (nxt_cost, tmp_y, tmp_x))
    print("Problem %d:"%a ,cost_lst[N-1][N-1])


N = int(input())
a = 1
while (N != 0):
    lst = []
    for i in range (N) :
        tmp = list(map(int, input().split()))
        lst.append(tmp)
    #print(lst)
    Dijkstra(a)
    a += 1
    N = int(input())