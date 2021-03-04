import sys

N, M = map(int, sys.stdin.readline().split())
trace_lst = []
for i in range (N+1) :
    trace_lst.append([])
for i in range (M) :
    tmp_lst = list(map(int, sys.stdin.readline().split()))
    trace_lst[tmp_lst[0]].append(tmp_lst[1])
    trace_lst[tmp_lst[1]].append(tmp_lst[0])
K = int(sys.stdin.readline())
visited_lst = [0] * (N+1)
devastated_lst = list(map(int, sys.stdin.readline().split()))
for i in devastated_lst :
    visited_lst[i] = 1
boom_lst = []

for i in devastated_lst :
    for j in trace_lst[i] :
        if j not in devastated_lst : # 파괴되지 않은 도시라면 다음 i로
            break
    else :
        for j in trace_lst[i] :
            visited_lst[j] = 2
        visited_lst[i] = 2
        boom_lst.append(i)

for i in visited_lst :
    if i == 1 :
        print(-1)
        break
else :
    print(len(boom_lst))
    for j in sorted(boom_lst) :
        print(j, end =" ")




