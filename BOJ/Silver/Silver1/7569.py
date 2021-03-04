from collections import deque
import sys

M, N, H = map(int, sys.stdin.readline().split())
tomato_lst = deque()
for h in range (H) :
    tmp1_lst = deque()
    for i in range (N) :
        tmp2_lst = deque()
        tmp2_lst.extend(list(map(int, sys.stdin.readline().split())))
        tmp1_lst.append(tmp2_lst)
    tomato_lst.append(tmp1_lst)

## 안익은 토마토가 없는 경우
for h in range (H) :
    for i in range (N) :
        for j in range (M) :
            if tomato_lst[h][i][j] == 0 :
                break
        else : continue
        break
    else : continue
    break
else :
    print("0")
    exit()

lst = deque()
for h in range (H) :
    for i in range (N) :
        for j in range (M) :
            if tomato_lst[h][i][j] == 1 :
                tmp_lst = deque()
                tmp_lst.extend([h,i,j,0])
                lst.append(tmp_lst)

move_h_lst = [1, -1]
move_y_lst = [0, 0, 1, -1]
move_x_lst = [1, -1, 0, 0]

def BFS() :
    while len(lst) != 0 :
        now = lst.popleft()
        cost = now[3]
        h = now[0]
        y = now[1]
        x = now[2]
        for i in range (4) :
            tmp_x = x + move_x_lst[i]
            tmp_y = y + move_y_lst[i]
            if 0 <= tmp_x < M and 0 <= tmp_y < N :
                if tomato_lst[h][tmp_y][tmp_x] == 0 :
                    tmp_lst = deque()
                    tmp_lst.extend([h, tmp_y, tmp_x, cost+1])
                    lst.append(tmp_lst)
                    tomato_lst[h][tmp_y][tmp_x] = 1
        for i in range (2) :
            tmp_h = h + move_h_lst[i]
            if 0 <= tmp_h < H :
                if tomato_lst[tmp_h][y][x] == 0 :
                    tmp_lst = deque()
                    tmp_lst.extend([tmp_h, y, x, cost+1])
                    lst.append(tmp_lst)
                    tomato_lst[tmp_h][y][x] = 1

        # 출력
        # print("")
        # for h in range(H) :
        #     for i in range (N) :
        #         for j in range (M) :
        #             print(tomato_lst[h][i][j], end=" ")
        #         print("")
    return cost

cost = BFS()
for h in range (H) :
    for i in range (N) :
        for j in range (M) :
            if tomato_lst[h][i][j] == 0 :
                print("-1")
                exit()
print(cost)


# 출력
# for h in range(H) :
#     for i in range (N) :
#         for j in range (M) :
#             print(tomato_lst[h][i][h], end=" ")
#         print("")