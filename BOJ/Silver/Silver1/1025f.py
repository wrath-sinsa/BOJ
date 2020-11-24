N, M = map(int, input().split()) # 0 <= N , M <= 9
lst = []
for i in range (N) :
    tmp_lst = list(str(input()))
    lst.append(tmp_lst)
if N == 0 or M == 0 :
    print(-1)
else :
    for i in range (len(lst)) :
        for j in range (len(lst[0])) :
            print(lst[i][j], end = " ")
        print("")
    print(lst)
