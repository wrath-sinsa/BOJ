N, M, K = map(int,input().split())
lst = []
for i in range (N) :
    tmp_lst = list(map(int,input().split()))
    lst.append(tmp_lst)
print (lst)    
s_lst = [0] * N
for i in range (M) :
    for j in range (N) :
        s_lst[j] += lst[j][i]
        if s_lst[j] >= K :
            print(j+1, i+1)
            break
    else :
        continue
    break
