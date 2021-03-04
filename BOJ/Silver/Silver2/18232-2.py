import sys

# 변수 설정
N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())
# tp_lst
tp_lst = []
for i in range (N+1) :
    tp_lst.append([]) 
visited_lst = [0] * (N+1)
#print(tp_lst, visited_lst)
for i in range (M) :
    tmp_lst = list(map(int,sys.stdin.readline().split()))
    tp_lst[tmp_lst[0]].append(tmp_lst[1])
    tp_lst[tmp_lst[1]].append(tmp_lst[0])
#print(tp_lst)
visited_lst = [0] * (N+1)
lst = [[S,0]]
visited_lst[S] = 1

while len(lst) != 0 :
    now = lst.pop(0)
    where = now[0]
    cost = now[1]
    
    if where == E : break
    
    if where + 1 <= N and visited_lst[where+1] == 0:
        lst.append([where+1, cost+1])
        visited_lst[where+1] = 1
    if where - 1 > 0 and visited_lst[where-1] == 0:
        lst.append([where-1, cost+1])   
        visited_lst[where-1] = 1
    for i in tp_lst[where] :
        if visited_lst[i] == 0 :
            lst.append([i, cost+1])
            visited_lst[i] = 1

print(cost)