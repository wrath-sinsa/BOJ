# DFS
N = int(input())
lst = []
for i in range (N) :
    tmp_lst = list(map(int, input()))
    lst.append(tmp_lst)

move_to_x_lst = [0, 0, -1, 1]
move_to_y_lst = [1, -1, 0, 0]


def DFS(x, y) :
    global cnt
    for i in range (4) :
        tmp_x = x + move_to_x_lst[i]
        tmp_y = y + move_to_y_lst[i]
        if 0 <= tmp_x < N and 0 <= tmp_y < N :
            if lst[tmp_y][tmp_x] == 1 :
                lst[tmp_y][tmp_x] = 2 # 체크용
                cnt += 1
                DFS(tmp_x, tmp_y)

global cnt
s = 0
cnt_lst = []
for i in range (N) :
    for j in range (N) :
        if lst[i][j] == 1 :
            lst[i][j] = 2
            s += 1
            cnt = 1
            DFS(j, i)
            cnt_lst.append(cnt)
print(s)
for i in sorted(cnt_lst) :
    print (i)


# 프린트
# for j in lst :
#     for k in j :
#         print (k, end= " ")
#     print("")
# print("")