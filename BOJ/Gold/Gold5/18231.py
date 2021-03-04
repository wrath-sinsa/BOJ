import sys

N, M = map(int, sys.stdin.readline().split())
trace_lst = []
for i in range (M) :
    tmp_lst = list(map(int, sys.stdin.readline().split()))
    trace_lst.append(tmp_lst)
K = int(sys.stdin.readline())
devastated_lst = list(map(int, sys.stdin.readline().split()))
boom_lst = []

for j in devastated_lst :
    now = j
    for i in trace_lst : 
        if i[0] == now :
            if i[1] in devastated_lst : # i[1]이 황폐화되었는가?
                continue # 그렇다면 다음것 확인
            else : break # 그렇지 않다면 다음 황폐화된 곳 확인해야함.
            # for문을 break로 나간후 while문을 continue// 그냥하면 될듯
        if i[1] == now :
            if i[0] in devastated_lst : # i[0]가 황폐화되었는가?
                continue # 그렇다면 다음것 확인
            else : break # 그렇지 않다면 다음 황폐화된 곳 확인해야함.
            # for문을 break로 나간후 while문을 continue
    else : # 주변이 모두 황폐화되어 for문을 다 지났다면// 그냥하면 됨
        boom_lst.append(now)

if len(boom_lst) == 0 :
    print(-1)
else :
    for i in sorted(boom_lst) :
        print (i, end = " ")