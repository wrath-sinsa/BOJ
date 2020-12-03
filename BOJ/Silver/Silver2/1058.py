# 1. 두사람이 친구일 경우
# 2. 두사람이

N = int(input())
lst = []
for i in range (N) :
    tmp_lst = list(str(input()))
    lst.append(tmp_lst)
cnt_lst = [0] * N
for i in range (N) :
    tmp_cnt = 0
    for j in range (N) :
        if lst[i][j] == "Y" :
            cnt_lst[i] += 1
        elif i < j : # "N" 이고 자기자신이 아닌경우이며 이미 계산했던 경우 스킵
            for n in range (N) : 
                if lst[i][n] == "Y" and lst[i][n] == lst[j][n] : # j번째 사람의 친구일때 i도 겹치는가?
                    cnt_lst[i] += 1
                    cnt_lst[j] += 1
                    break
print(max(cnt_lst))
