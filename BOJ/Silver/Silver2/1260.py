N, M, V = map(int, input().split())

trace_lst = []
for i in range (N+1) :
    trace_lst.append([])
for i in range (M) :
    trace = list(map(int, input().split()))
    trace_lst[trace[0]].append(trace[1])
    trace_lst[trace[1]].append(trace[0])
for i in trace_lst :
    i.sort()

## DFS
used_lst_DFS = [0] * (N+1)

lst = [V]
ans = [] # 전역 가능

def DFS() :
    now = lst[0]
    used_lst_DFS[now] = 1
    ans.append(lst.pop(0))
    for i in trace_lst[now] :
        if used_lst_DFS[i] == 0:
            lst.append(i)
            used_lst_DFS[i] = 1
            DFS()

DFS()
for i in ans :
    print (i, end = " ")
print("")

## BFS
used_lst_BFS = [0] * (N+1)

def BFS() :
    lst = [V]
    ans = [] # 지역, 전역 가능
    while len(lst) != 0 :
        now = lst[0]
        used_lst_BFS[now] = 1
        ans.append(lst.pop(0))
        for i in trace_lst[now] :
            if used_lst_BFS[i] == 0 :
                lst.append(i)
                used_lst_BFS[i] = 1
    return ans

for i in BFS() :
    print (i, end = " ")
