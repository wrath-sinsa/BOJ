import sys
from collections import deque 
input = sys.stdin.readline
## 이동
move_x_lst = [0,0,-1,1]
move_y_lst = [1,-1,0,0]
##
def BFS(key, door) :
    ## 풀이에 사용할 lst
    cnt = 0
    while len(lst) != 0 :
        now = lst.popleft()
        x = now[1]
        y = now[0]
        if value_lst[y][x] == "$" : cnt += 1
        for i in range (4) : # 이동판정
            tmp_x = x + move_x_lst[i]
            tmp_y = y + move_y_lst[i]
            if 0 <= tmp_x < M and 0 <= tmp_y < N :
                if used[tmp_y][tmp_x] == 0 : # 이동한 지역이 아닐때
                    if value_lst[tmp_y][tmp_x] == "*" : continue 
                    elif ord('A') <= ord(value_lst[tmp_y][tmp_x]) <= ord('Z') :
                        if (key & 1 << (ord(value_lst[tmp_y][tmp_x])-ord('A')) == 0) :# 열쇠가 없을경우
                            door[ord(value_lst[tmp_y][tmp_x])-ord('A')].append((tmp_y, tmp_x))
                            continue
                    elif ord('a') <= ord(value_lst[tmp_y][tmp_x]) <= ord('z') :
                        key = key | 1 << (ord(value_lst[tmp_y][tmp_x])-ord('a'))
                        while len(door[ord(value_lst[tmp_y][tmp_x])-ord('a')]) != 0 :
                            y = door[ord(value_lst[tmp_y][tmp_x])-ord('a')][0][0]
                            x = door[ord(value_lst[tmp_y][tmp_x])-ord('a')][0][1]
                            door[ord(value_lst[tmp_y][tmp_x])-ord('a')].popleft()
                            lst.append((y, x))
                            used[y][x] = 1
                    lst.append((tmp_y, tmp_x))
                    used[tmp_y][tmp_x] = 1       
        # 출력 
        # for i in range (N) :
        #     for j in range (M) :
        #         print(used[i][j], end = " ")
        #     print("")
        # print("")                    
    return cnt # 정답 처리



T = int(input())
while (T) :
    #입력
    N, M = map(int, input().split())
    door = [deque() for i in range (26)]
    value_lst = [[0]*M for i in range (N)]
    lst = deque()
    key = 0
    used = [[0]*M for j in range (N) ]
    for i in range (N) :
        v = input().rstrip()
        for j in range (M) :
            value_lst[i][j] = v[j]
            if i == 0 or i == N - 1 or j == 0 or j == M - 1 : # 테두리
                if v[j] == '*' : continue
                elif ord(v[j]) >= ord('A') and ord(v[j]) <= ord('Z') :
                    door[ord(v[j]) - ord('A')].append((i,j)) 
                    continue
                elif ord(v[j]) >= ord('a') and ord(v[j]) <= ord('z') : #열쇠 비트마스킹
                    key = key | 1 << (ord(v[j])-ord('a'))
                lst.append((i,j))
                used[i][j] = 1

    k = input().rstrip()
    if k != "0" :
        for i in range (len(k)) :
            #print(ord(k[i])-ord('a'))
            key = key | 1 << (ord(k[i])-ord('a'))
            while len(door[ord(k[i])-ord('a')]) != 0 :
                y = door[ord(k[i])-ord('a')][0][0]
                x = door[ord(k[i])-ord('a')][0][1]
                door[ord(k[i])-ord('a')].popleft()
                lst.append((y, x))
                used[y][x] = 1
    print(BFS(key, door))
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