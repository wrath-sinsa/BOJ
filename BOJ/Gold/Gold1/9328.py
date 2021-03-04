import sys
from collections import deque 
input = sys.stdin.readline
## 이동
move_x_lst = [0,0,-1,1]
move_y_lst = [1,-1,0,0]
chk = 'abcdefghijklmnopqrstuvwxyz'
##
def BFS(key) :
    ## 풀이에 사용할 lst
    lst = deque()
    # 테두리 열쇠가 있을 경우, "."" 일경우
    cnt = side(lst, key, 0)
    while len(lst) != 0 :
        now = lst.popleft()
        x = now[1]
        y = now[0]
        for i in range (4) : # 이동판정
            tmp_x = x + move_x_lst[i]
            tmp_y = y + move_y_lst[i]
            if 0 <= tmp_x < M and 0 <= tmp_y < N :
                if used[tmp_y][tmp_x] == 0 : # 이동한 지역이 아닐때
                    
                    if value_lst[tmp_y][tmp_x] == "$" :  # 정답처리
                        used[tmp_y][tmp_x] = 1
                        lst.append((tmp_y, tmp_x))
                        cnt += 1
                    
                    if value_lst[tmp_y][tmp_x] == "." : # 이동 할수 있을 경우
                        used[tmp_y][tmp_x] = 1
                        lst.append((tmp_y, tmp_x))

                    for j in range (26) :
                        if value_lst[tmp_y][tmp_x] == chk[j] : # 열쇠를 먹을경우
                            # 테두리 열쇠가 있을 경우, "."" 일 경우
                            used[tmp_y][tmp_x] = 1
                            lst.append((tmp_y, tmp_x))
                            key = key | 1 << ord(chk[j]) - 97 
                            # print(wall)
                            for k in range (len(wall)) : # 못들어간 벽을 돌면서
                                if wall[k][2] == chk[j].upper() : # 벽이 열쇠랑 같다면
                                    used[wall[k][0]][wall[k][1]] = 1 
                                    lst.append((wall[k][0], wall[k][1]))
                                    #print(1)
                            # print(wall)
                        if value_lst[tmp_y][tmp_x] == chk[j].upper() : # 문을 만났을 경우
                            if key & 1 << ord(chk[j]) - 97 != 0 : # 열쇠를 갖고 있을경우
                                used[tmp_y][tmp_x] = 1
                                lst.append((tmp_y, tmp_x))
                            else : wall.append((tmp_y, tmp_x, value_lst[tmp_y][tmp_x]))
        # 출력 
        # for i in range (N) :
        #     for j in range (M) :
        #         print(used[i][j], end = " ")
        #     print("")
        # print("")                    
    return cnt # 정답 처리

def side(d, bit, cnt) :
    for j in range (1,M-1):
        # 위쪽
        if value_lst[0][j] == "*" : pass
        elif value_lst[0][j] == "$" : 
            cnt += 1
            d.append((0,j))
            used[0][j] = 1
        elif value_lst[0][j] == "." :
            d.append((0,j))
            used[0][j] = 1
        elif 0 <= ord(value_lst[0][j])-ord("a") <= 26  :
            d.append((0,j))
            used[0][j] = 1
        elif bit & 1 << ord(value_lst[0][j]) - 65 != 0 : # 열쇠가 있는 경우
            d.append((0,j))
            used[0][j] = 1
        elif bit & 1 << ord(value_lst[0][j]) - 65 == 0 : # 열쇠가 없는 경우
            wall.append((0,j,value_lst[0][j])) # 벽에 저장
        # 아래쪽
        if value_lst[N-1][j] == "*" : pass  
        elif value_lst[N-1][j] == "$" :
            cnt += 1
            d.append((N-1,j))
            used[N-1][j] = 1
        elif 0 <= ord(value_lst[N-1][j])-ord("a") <= 26 :
            d.append((N-1,j))
            used[N-1][j] = 1
        elif value_lst[N-1][j] == "." :
            d.append((N-1,j))
            used[N-1][j] = 1
        elif bit & 1 << ord(value_lst[N-1][j]) - 65 != 0 : # 열쇠가 있는 경우
            d.append((N-1,j))
            used[N-1][j] = 1
        elif bit & 1 << ord(value_lst[N-1][j]) - 65 == 0 : # 열쇠가 없는 경우
            wall.append((N-1,j,value_lst[N-1][j])) # 벽에 저장
    
    for i in range (1, N-1) :
        # 왼쪽
        if value_lst[i][0] == "*" : pass  
        elif value_lst[i][0] == "$" :
            cnt+=1
            d.append((i,0))
            used[i][0] = 1
        elif value_lst[i][0] == "." :
            d.append((i,0))
            used[i][0] = 1
        elif 0 <= ord(value_lst[i][0])-ord("a") <= 26 :
            d.append((i,0))
            used[i][0] = 1
        elif bit & 1 << ord(value_lst[i][0]) - 65 != 0 : # 열쇠가 있는 경우
            d.append((i,0))
            used[i][0] = 1
        elif bit & 1 << ord(value_lst[i][0]) - 65 == 0 : # 열쇠가 없는 경우
            wall.append((i,0,value_lst[i][0])) # 벽에 저장
        # 오른쪽
        if value_lst[i][M-1] == "*" : pass
        elif value_lst[i][M-1] == "$" :
            cnt += 1
            d.append((i,M-1))
            used[i][M-1] = 1
        elif value_lst[i][M-1] == "." :
            d.append((i,M-1))
            used[i][M-1] = 1
        elif 0 <= ord(value_lst[i][M-1])-ord("a") <= 26 :
            d.append((i,M-1))
            used[i][M-1] = 1
        elif bit & 1 << ord(value_lst[i][M-1]) - 65 != 0 : # 열쇠가 있는 경우
            d.append((i,M-1))
            used[i][M-1] = 1
        elif bit & 1 << ord(value_lst[i][M-1]) - 65 == 0 : # 열쇠가 없는 경우
            wall.append((i,M-1,value_lst[i][M-1])) # 벽에 저장
    return cnt

def bitmask(key) :
    if key == "0" :
        return 0
    bit = 0
    for i in range (len(key)) :
        bit = bit | 1 << ord(key[i]) - 97
    return bit

T = int(input())
while (T) :
    #입력
    N, M = map(int, input().split())

    value_lst = list()
    for i in range (N) :
        v = list(input().rstrip())
        value_lst.append(v)
    #print(value_lst)
    used = [[0]*M for j in range (N) ]
    key = bitmask(input().rstrip())
    wall = list()
    #print("key :", bin(key)[2:])
    #print("answer :", BFS(key))
    print(BFS(key))
    T -= 1
# print(value_lst)

# 출력 
# for i in range (N) :
#     for j in range (M) :
#         print(tomato_lst[i][j], end = "")
#     print("")
# print("")

# 1. 키를 얻을때마다 키에따른 used를 이용하려했음. >> used 1억 * 100 * 100 의 공간복잡도
# 2. 키를 전체 공유로 // 
# 2. 벽을 만날때마다 리스트에 저장, 키를 얻는다면 for문 돌려서 열쇠얻었다면 덱 앞으로 이동.
#  

## review 
# 처음 조건 이걸로 씹가능,,,
# 테두리 처리 아름다워,,
# if ((i == 0) || (i == w - 1) || (j == 0) || (j == h - 1))
#                 {
#                     if (str[j] == '*') continue;
#                     else if (str[j] >= 'A' && str[j] <= 'Z') {
#                         door[str[j] - 'A'].push(make_pair(i, j)); continue;
#                     }
#                     else if (str[j] >= 'a' && str[j] <= 'z') key[str[j] - 'a'] = true;
#                     q.push(make_pair(i, j));
#                     visited[i][j] = true;
#                 }