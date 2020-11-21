# T = int(input())
# for i in range (T):
#     M, N, K = map(int, input().split())
#     lst = []
#     for y in range (N) :
#         tmp = []
#         cnt = 0
#         for x in range (M) :
#             tmp.append(0)
#         lst.append(tmp)
#     # print (lst)
#     for j in range (K) :
#         X, Y = map(int, input().split())
#         lst[Y][X] = 1
#     # print(lst)

# 1 이면 들어감
def find_cabbage(dot) :
    # 좌 상 우 하 순
    find_lst_x = [-1, 0, 1, 0]
    find_lst_y = [0 , -1, 0, 1]
    # print(x, y)
    # print("점 위치는", dot[0], dot[1])
    lst[dot[1]][dot[0]] = 2
    tmp_dot = dot[:]
    for a, b in zip(find_lst_x, find_lst_y) :
        tmp_dot[0] = dot[0] + a
        tmp_dot[1] = dot[1] + b
        if tmp_dot[0] < 0 or tmp_dot[1] < 0 or tmp_dot[0] >= M or tmp_dot[1] >= N :
            continue
        else : 
            if lst[tmp_dot[1]][tmp_dot[0]] == 1 :
                find_cabbage(tmp_dot)
    
## 사용자 초기화
M, N = 10, 8
cnt = 0
lst= [[1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 1, 1, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# 배추 위치 출력
# for Y in range (N) :
#     for X in range (M) :
#         print (lst[Y][X], end = " ")
#     print("")
# print ("\n")

for Y in range (N) :
    for X in range (M) :
        if lst[Y][X] == 1:
            dot = [X, Y]
            find_cabbage(dot)
            cnt += 1
            # print (cnt)

# 벌레 커버 가능 배추 위치 출력
# for Y in range (N) :
#     for X in range (M) :
#         print (lst[Y][X], end = " ")
#     print("")

print (cnt)

### 
# tmp_lst에 점들을 넣고 각각 뒤져가며 점이 있으면 while문을 또 써서...
# 하려했지만 굳이 distance를 구할필요 없이 상하좌우로 x값 y값만 바꿔주는걸로 바꿈


# while len(tmp_lst) != 0:
#     for n in range (len(tmp_lst)) :
#         tmp = tmp_lst.pop(0)
#         distance = abs(tmp[0] - tmp_lst[n][0]) + abs(tmp[1]- tmp_lst[n][1])
#         if distance == 1 :
#             tmp_lst.pop(n)
#             tmp2_lst.append(tmp_lst[n])
#     while len(tmp2_lst) != 0:
#         tmp_lst # while 이 반복되므로 재귀함수 써야겠다....
#     print(tmp2_lst)

