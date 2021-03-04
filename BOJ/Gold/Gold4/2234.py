import sys
from collections import deque 
input = sys.stdin.readline

M, N = map(int, input().split())

value_lst = list()
for i in range (N) :
    v = list(map(int, input().split()))
    value_lst.append(v)

## 이동
move_x_lst = [-1,0,1,0]
move_y_lst = [0,-1,0,1]
used = [[-1] *M for i in range (N)]
##
def BFS() :
    ## 풀이에 사용할 lst
    lst = deque()
    size = list() # 방
    Nb = 0 # 방 번호
    for i in range (N) :
        for j in range (M) :
            if used[i][j] == -1 :
                lst.append((i,j))
                used[i][j] = Nb
                tmp = 0
                while len(lst) != 0 :
                    now = lst.popleft()
                    x = now[1]
                    y = now[0]
                    tmp += 1
                    for k in range (4) :
                        if value_lst[y][x] & 1 << k == 0 : # 벽이 없을때
                            tmp_x = x + move_x_lst[k]
                            tmp_y = y + move_y_lst[k]
                            if 0 <= tmp_x < M and 0 <= tmp_y < N :
                                if used[tmp_y][tmp_x] == -1 :
                                    used[tmp_y][tmp_x] = Nb
                                    lst.append((tmp_y, tmp_x))
                size.append(tmp)
                Nb += 1
                #print(size, Nb)
                # 출력 
                # for _ in range (N) :
                #     for __ in range (M) :
                #         print(used[_][__], end = " ")
                #     print("")
                # print("")
    maximum = 0
    for i in range (N) :
        for j in range (M) :
            for k in range (2,4) :
                y = i + move_y_lst[k]
                x = j + move_x_lst[k]
                if 0 <= y < N and 0 <= x < M :
                    if used[i][j] != used[y][x] :
                        tmp = size[used[i][j]] + size[used[y][x]]
                        if tmp > maximum : maximum = tmp
    #print(size)
    print(len(size))
    print(max(size))
    print(maximum)

# 정답처리
BFS()
# 출력 
# for i in range (N) :
#     for j in range (M) :
#         print(tomato_lst[i][j], end = "")
#     print("")
# print("")