N = int(input())
T = int(input())

trace_lst = []
for i in range (N+1) :
    trace_lst.append([])
for i in range (T) :
    trace = list(map(int, input().split()))
    trace_lst[trace[0]].append(trace[1])
    trace_lst[trace[1]].append(trace[0])

used_lst = [0] * (N+1)

lst = [1]
used_lst[1] = 1
def BFS() :
    cnt = 0
    while len(lst) != 0 :
        now = lst.pop(0)
        for i in trace_lst[now] :
            if used_lst[i] == 0 :
                lst.append(i)
                used_lst[i] = 1 
                cnt += 1
    return cnt

print(BFS())