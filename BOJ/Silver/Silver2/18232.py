import sys

# 변수 설정
N, M = map(int, sys.stdin.readline().split())
S, E = map(int, sys.stdin.readline().split())
lst = []
tp_lst = []
visited_lst = [0] * (N+1)
for i in range (M) :
    tmp_lst = list(map(int,sys.stdin.readline().split()))
    tp_lst.append(tmp_lst)

lst.append([S, 0])
visited_lst[S] = True

while len(lst) != 0 :
    now = lst[0] ## init [S, 0]
    where = now[0]
    cost = now[1]
    lst.pop(0)

    if where == E : break #도착시 소요시간 반환
    if where > 1 and visited_lst[where-1] == False :
        lst.append([where-1, cost+1])
        visited_lst[where-1] == True
    if where < N and visited_lst[where+1] == False :
        lst.append([where+1, cost+1])
        visited_lst[where+1] == True
    for i in tp_lst :
        if where == i[0] and visited_lst[i[1]] == False :
            lst.append([i[1], cost+1])
            visited_lst[i[1]] == True
print(cost)