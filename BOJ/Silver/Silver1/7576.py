import sys
from collections import deque 

M, N = map(int, sys.stdin.readline().split())

tomato_lst = deque()
for i in range (N) :
    tomato = deque(map(int, sys.stdin.readline().split()))
    tomato_lst.append(tomato)

## 처음부터 다 익어있는 경우
for i in range (N) : #최악의 경우 O(NM)
    for j in range (M) :
        if tomato_lst[i][j] == 0 :
            break
    else : continue
    break
else :
    print(0)
    exit()

## 풀이에 사용할 lst
lst = deque()
for i in range (N) : # O(NM)
    for j in range (M) :
        if tomato_lst[i][j] == 1 :
            lst.append([i, j, 0])

## 이동
move_x_lst = [0,0,-1,1]
move_y_lst = [1,-1,0,0]

##
def BFS() :
    while len(lst) != 0 :
        now = lst.popleft()
        day = now[2]
        x = now[1]
        y = now[0]
        for i in range (4) :
            tmp_x = x + move_x_lst[i]
            tmp_y = y + move_y_lst[i]
            if 0 <= tmp_x < M and 0 <= tmp_y < N :
                if tomato_lst[tmp_y][tmp_x] == 0 :
                    tomato_lst[tmp_y][tmp_x] = 1
                    lst.append([tmp_y, tmp_x, day+1])
        # 출력 
        # for i in range (N) :
        #     for j in range (M) :
        #         print(tomato_lst[i][j], end = " ")
        #     print("")
        # print("")
    return day

day = BFS()

# 정답처리
for i in range (N) :
    for j in range (M) :
        if tomato_lst[i][j] == 0 :
            print(-1)
            exit()
print (day)

# 출력 
# for i in range (N) :
#     for j in range (M) :
#         print(tomato_lst[i][j], end = "")
#     print("")
# print("")