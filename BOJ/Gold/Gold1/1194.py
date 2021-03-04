import sys
from collections import deque 
input = sys.stdin.readline

N, M = map(int, input().split())

value_lst = list()
for i in range (N) :
    v = list(input().rstrip())
    value_lst.append(v)
# print(value_lst)
## 이동
move_x_lst = [0,0,-1,1]
move_y_lst = [1,-1,0,0]
chk = ['a', 'b', 'c', 'd', 'e', 'f']
used = [[[0]*M for j in range (N) ] for i in range (64)]
##
def BFS() :
    ## 풀이에 사용할 lst
    lst = deque()

    for i in range (N) :
        for j in range (M) :
            if value_lst[i][j] == "0" :
                lst.append((i,j,0,0))
                value_lst[i][j] = "."
                used[0][i][j] = 1
                break
        else : continue
        break

    while len(lst) != 0 :
        now = lst.popleft()
        x = now[1]
        y = now[0]
        bits = now[2]
        cnt = now[3]
        
        for i in range (4) : # 이동판정
            tmp_x = x + move_x_lst[i]
            tmp_y = y + move_y_lst[i]
            if 0 <= tmp_x < M and 0 <= tmp_y < N :
                if used[bits][tmp_y][tmp_x] == 0 : # 이동한 지역이 아닐때
                    
                    if value_lst[tmp_y][tmp_x] == "1" : return cnt +1 # 정답처리
                    
                    if value_lst[tmp_y][tmp_x] == "." : # 이동 할수 있을 경우
                        #value_lst[tmp_y][tmp_x] = 
                        used[bits][tmp_y][tmp_x] = 1
                        lst.append((tmp_y, tmp_x, bits, cnt+1))

                    for j in range (6) :
                        if value_lst[tmp_y][tmp_x] == chk[j] : # 열쇠를 먹을경우
                            #value_lst[tmp_y][tmp_x] = 
                            used[bits][tmp_y][tmp_x] = 1
                            used[bits | 1 << ord(chk[j]) - 97][tmp_y][tmp_x] = 1
                            lst.append((tmp_y, tmp_x, bits | 1 << ord(chk[j]) - 97, cnt+1))
                        if value_lst[tmp_y][tmp_x] == chk[j].upper() : # 문을 만났을 경우
                            #value_lst[tmp_y][tmp_x] = 
                            #print(bits & 1 << ord(chk[j]) - 97)
                            if bits & 1 << ord(chk[j]) - 97 != 0 : # 열쇠를 갖고 있을경우
                                used[bits][tmp_y][tmp_x] = 1
                                lst.append((tmp_y, tmp_x, bits, cnt+1))
    return -1 # 정답 처리
        # 출력 
        # for i in range (N) :
        #     for j in range (M) :
        #         print(tomato_lst[i][j], end = " ")
        #     print("")
        # print("")

# 정답처리
print(BFS())

# 출력 
# for i in range (N) :
#     for j in range (M) :
#         print(tomato_lst[i][j], end = "")
#     print("")
# print("")

# 힙으로 푸는게 나은가?
# 비트마스킹 값 전달