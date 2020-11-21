def find_cabbage(dot) :

    find_lst_x = [-1, 0, 1, 0]
    find_lst_y = [0 , -1, 0, 1]
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

T = int(input())
for i in range (T):
    M, N, K = map(int, input().split())
    cnt = 0
    lst = []
    for y in range (N) :
        tmp = []
        for x in range (M) :
            tmp.append(0)
        lst.append(tmp)
    # print (lst)
    for j in range (K) :
        X, Y = map(int, input().split())
        lst[Y][X] = 1
    # print(lst)
    # 배추 위치 출력
    for Y in range (N) :
        for X in range (M) :
            print (lst[Y][X], end = " ")
        print("")
    print ("\n")

    for Y in range (N) :
        for X in range (M) :
            if lst[Y][X] == 1:
                dot = [X, Y]
                find_cabbage(dot)
                cnt += 1
    print(cnt)

    for Y in range (N) :
        for X in range (M) :
            print (lst[Y][X], end = " ")
        print("")
    print ("\n")

#Review
# import sys
# sys.setrecursionlimit(10000)
# 재귀함수의 한도를 늘려줌