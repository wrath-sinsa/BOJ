N = int(input())
lst = [list(map(int,input().split())) for i in range (N)]
global cnt0, cnt1
cnt0 = 0
cnt1 = 0
def paper(lst, n) :
    global cnt0, cnt1
    chk0 = 0
    chk1 = 0
    for i in range(n) :
        for j in range(n) :
            if lst[i][j] == 0 :
                chk0 = 1
            if lst[i][j] == 1 :
                chk1 = 1
        else : continue
        break
    half = n//2
    times_lst_y = [0, half, 0, half, half, n, half, n]
    times_lst_x = [0, half, half, n, 0, half, half, n]
    if chk0 == 1 and chk1 == 1 :
        for i in range (4) :
            tmp_lst = [lst[x][times_lst_x[2*i]:times_lst_x[2*i+1]] for x in range (times_lst_y[2*i], times_lst_y[2*i+1])]
            paper(tmp_lst, half)
    elif chk1 == 1 : cnt1 += 1
    elif chk0 == 1 : cnt0 += 1

paper(lst, N)
print(cnt0, cnt1)