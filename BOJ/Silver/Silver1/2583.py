import sys
from collections import deque 
input = sys.stdin.readline

N, M, K = map(int, input().split())

value_lst = list()
for i in range (K) :
    v = list(map(int, input().split()))
    value_lst.append(v)

# 모눈 종이 정리
base = [[0]*M for i in range (N)]
for i in range (K) :
    for j in range (value_lst[i][1], value_lst[i][3]) :
        for k in range (value_lst[i][0], value_lst[i][2]) :
            base[j][k] = 1

#출력 
# for i in range (N) :
#     for j in range (M) :
#         print(base[i][j], end = "")
#     print("")
# print("")

## 풀이에 사용할 lst
lst = deque()

## 이동
move_x_lst = [0,0,-1,1]
move_y_lst = [1,-1,0,0]

##
def BFS() :
    s = 1
    while len(lst) != 0 :
        now = lst.popleft()
        x = now[1]
        y = now[0]
        for i in range (4) :
            tmp_x = x + move_x_lst[i]
            tmp_y = y + move_y_lst[i]
            if 0 <= tmp_x < M and 0 <= tmp_y < N :
                if base[tmp_y][tmp_x] == 0 :
                    base[tmp_y][tmp_x] = 2
                    s += 1
                    lst.append((tmp_y, tmp_x))
        # 출력 
        # for i in range (N) :
        #     for j in range (M) :
        #         print(base[i][j], end = " ")
        #     print("")
        # print("")

    return s

# 정답처리
count = 0
ans = list()
for i in range (N) :
    for j in range(M) :
        if base[i][j] == 0 :
            lst.append((i,j))
            base[i][j] = 2
            ans.append(BFS())
            count += 1
print (count)
for i in sorted(ans) : print (i, end = " ")

# 출력 
# for i in range (N) :
#     for j in range (M) :
#         print(tomato_lst[i][j], end = "")
#     print("")
# print("")