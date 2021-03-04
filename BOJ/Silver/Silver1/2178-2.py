import sys

#DFS
N, M = map(int, sys.stdin.readline().split())
maze_lst = []
for i in range (N) :
    maze = list(map(int, sys.stdin.readline()[:-1]))
    maze_lst.append(maze)
movex_lst = [0,0,1,-1]
movey_lst = [1,-1,0,0]

lst = [[0,0,1]]

def BFS() :
    while len(lst) != 0 :
        now = lst.pop(0)
        x = now[0]
        y = now[1]
        cnt = now[2]
        if x == M-1 and y == N-1 :
            return cnt
        for i in range (4) :
            tmp_x = x + movex_lst[i]
            tmp_y = y + movey_lst[i]
            if 0 <= tmp_x < M and 0 <= tmp_y < N :
                if maze_lst[tmp_y][tmp_x] == 1 :
                    maze_lst[tmp_y][tmp_x] = 0
                    lst.append([tmp_x,tmp_y,cnt+1])
print(BFS())


# 출력
# for i in maze_lst :
#     for j in i :
#         print (j)
#     print("")
# print("")