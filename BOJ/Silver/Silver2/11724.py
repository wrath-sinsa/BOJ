import sys
from collections import deque
N, M = map(int, sys.stdin.readline().split())

# 노드 초기화
nod_lst = [[] for i in range (N+1)] 
for i in range (M) :
    a, b = map(int, sys.stdin.readline().split())
    nod_lst[a].append(b)
    nod_lst[b].append(a)

used_lst = [0] * (N+1)

lst = deque()

def BFS() :
    while len(lst) != 0 :
        now = lst.popleft()
        for i in nod_lst[now] :
            if used_lst[i] == 0 :
                used_lst[i] = 1
                lst.append(i)

cnt = 0
for i in range (1, N+1) :
    if used_lst[i] == 0 :
        used_lst[i] = 1
        lst.append(i)
        BFS()
        cnt += 1
print (cnt)
