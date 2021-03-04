import sys

def duck(k, idx) :
    global s1, s2
    if k == P :

        if s1 <= E <= s2 :
            cal()
        return
    for i in range (N) :
        if used_lst[i] != 1 :
            if idx > i :
                continue
            used_lst[i] = 1
            s1 += lst[i][0]
            s2 += lst[i][1]
            duck(k + 1, i)
            s1 -= lst[i][0]
            s2 -= lst[i][1]
            used_lst[i] = 0

def cal() :
    global E
    global ans_lst
    for i in range (N) :
        if used_lst[i] == 1 :
            ans_lst[i] = lst[i][0]
    remain = E - sum(ans_lst)
    for i in range (N) :
        if used_lst[i] == 1 :
            x = lst[i][1]-lst[i][0]
            if remain >= x :
                ans_lst[i] = lst[i][1]
                remain -= x
            else :
                ans_lst[i] += remain
                remain = 0
            if remain == 0 :
                break
    for j in ans_lst :
        print (j, end=" ")
    exit()

# 변수 설정
global E
global ans_lst
N, P, E = map(int, sys.stdin.readline().split())
lst = []
for i in range (N) :
    tmp_lst = list(map(int, sys.stdin.readline().split()))
    lst.append(tmp_lst)
if N < P :
    print(-1)
    exit()
used_lst = [0] * N
ans_lst = [0] * N
global s1, s2
s1 = 0
s2 = 0
# 실행
duck(0, -1)
print(-1)