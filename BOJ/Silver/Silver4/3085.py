import sys
import heapq
from collections import deque
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
N = int(input())
candy = [list(input().rstrip()) for i in range (N)]
move_x = [-1 ,1]
move_y = [1, -1]
ans = 0
for i in range (N) :
    for j in range (N) :
        lst = deque()
        if j < N-1 :
            tmp = [[0]*N for i in range (N)]
            used = [[0]*N for i in range (N)]
            for _ in range (N) :
                for __ in range (N) :
                    tmp[_][__] = candy[_][__]
                    
            tmp[i][j], tmp[i][j+1] = tmp[i][j+1], tmp[i][j]
            lst.append((tmp[i][j], i, j))
            lst.append((tmp[i][j+1], i, j+1))
            used[i][j] = 1
            used[i][j+1] = 1
            a = 0
            while (lst) :
                #print(lst)
                c, y, x = lst.popleft()
                for _ in range (2) :
                    dx = x + move_x[_]
                    if 0 <= dx < N :
                        if tmp[y][dx] == c and used[y][dx] != 1 :
                            used[y][dx] = 1
                            lst.append((c, y, dx))
                            a += 1

            if a > ans : ans = a

        if i < N-1 :
            tmp = [[0]*N for i in range (N)]
            used = [[0]*N for i in range (N)]
            for _ in range (N) :
                for __ in range (N) :
                    tmp[_][__] = candy[_][__]

            tmp[i][j], tmp[i+1][j] = tmp[i+1][j], tmp[i+1][j]
            lst.append((tmp[i][j], i, j))
            lst.append((tmp[i+1][j], i+1, j))
            used[i][j] = 1
            used[i+1][j] = 1
            a = 0
            while (lst) :
                c, y, x = lst.popleft()
                for _ in range (2) :
                    dy = y + move_y[_]
                    if 0 <= dy < N :
                        if tmp[dy][x] == c and used[dy][x] != 1: 
                            used[dy][x] = 1
                            lst.append((c, dy, x))
                            a += 1
            if a > ans : ans = a
print(ans)