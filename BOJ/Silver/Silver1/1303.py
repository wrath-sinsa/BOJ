from collections import deque

N, M = map(int, input().split())
war_lst = [input() for i in range (M)]
used_lst = [[0] * (N) for i in range (M)]


move_x_lst = [0, 0, 1, -1]
move_y_lst = [1, -1, 0, 0]

global blue_S, white_S
blue_S = 0
white_S = 0

def BFS(color) :
    global blue_S, white_S
    cnt = 1
    while len(lst) != 0 :
        now = lst.popleft()
        # print(now)
        y = now[0]
        x = now[1]
        for i in range (4) :
            tmp_x = x + move_x_lst[i]
            tmp_y = y + move_y_lst[i]
            if 0 <= tmp_x < N and 0 <= tmp_y < M :
                # print(tmp_y, tmp_x, color)
                if used_lst[tmp_y][tmp_x] == 0 and war_lst[tmp_y][tmp_x] == color :
                    tmp_lst = deque()
                    tmp_lst.extend([tmp_y, tmp_x])
                    lst.append(tmp_lst)
                    used_lst[tmp_y][tmp_x] = 1
                    cnt += 1

    if color == "W" : white_S += cnt ** 2
    else : blue_S += cnt ** 2

lst = deque()
for i in range (M) :
    for j in range (N) :
        if used_lst[i][j] == 0 :
            tmp_lst = deque()
            tmp_lst.extend([i, j])
            used_lst[i][j] = 1
            lst.append(tmp_lst)
            BFS(war_lst[i][j])
print(white_S, blue_S)
