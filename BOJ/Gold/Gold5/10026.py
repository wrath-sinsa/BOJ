import sys
from collections import deque 
input = sys.stdin.readline

N = int(input())

value_lst = list()
for i in range (N) :
    v = list(input().rstrip())
    value_lst.append(v)

## 이동
move_x_lst = [0,0,-1,1]
move_y_lst = [1,-1,0,0]

##
def BFS1(a, b, c) :
    ## 풀이에 사용할 lst
    lst = deque()
    lst.append((a,b))
    used_lst[a][b] = 1
    while len(lst) != 0 :
        now = lst.popleft()
        x = now[1]
        y = now[0]
        for i in range (4) :
            tmp_x = x + move_x_lst[i]
            tmp_y = y + move_y_lst[i]
            if 0 <= tmp_x < N and 0 <= tmp_y < N :
                if value_lst[tmp_y][tmp_x] == c and used_lst[tmp_y][tmp_x] == 0 :
                    used_lst[tmp_y][tmp_x] = 1
                    lst.append((tmp_y, tmp_x))
        # 출력 
        # for i in range (N) :
        #     for j in range (M) :
        #         print(value_lst[i][j], end = " ")
        #     print("")
        # print("")
def BFS2(a, b, c) :

    ## 풀이에 사용할 lst
    lst = deque()
    lst.append((a,b))
    used_lst[a][b] = 1
    while len(lst) != 0 :
        now = lst.popleft()
        x = now[1]
        y = now[0]
        for i in range (4) :
            tmp_x = x + move_x_lst[i]
            tmp_y = y + move_y_lst[i]
            if 0 <= tmp_x < N and 0 <= tmp_y < N :
                if c == "R" or c == "G" :
                    if value_lst[tmp_y][tmp_x] == "R" or value_lst[tmp_y][tmp_x] == "G" :
                        if used_lst[tmp_y][tmp_x] == 0 :
                            used_lst[tmp_y][tmp_x] = 1
                            lst.append((tmp_y, tmp_x))
                else : # c== "B" 
                    if value_lst[tmp_y][tmp_x] == "B" and used_lst[tmp_y][tmp_x] == 0 :
                        used_lst[tmp_y][tmp_x] = 1
                        lst.append((tmp_y, tmp_x))
        # 출력 
        # for i in range (N) :
        #     for j in range (N) :
        #         print(value_lst[i][j], end = " ")
        #     print("")
        # print("")

# 정답처리
used_lst = [[0]*N for i in range (N)]
count1 =0
for i in range (N) :
    for j in range (N) :
        if used_lst[i][j] == 0 :
            BFS1(i, j, value_lst[i][j])
            count1 += 1

used_lst = [[0]*N for i in range (N)]
count2 = 0
for i in range (N) :
    for j in range (N) :
        if used_lst[i][j] == 0 :
            BFS2(i, j, value_lst[i][j])
            count2 += 1

print(count1, count2)
# 출력 
# for i in range (N) :
#     for j in range (M) :
#         print(value_lst[i][j], end = "")
#     print("")
# print("")