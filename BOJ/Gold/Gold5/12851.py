import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

used_lst = [100000] * 100001
used_lst[N] = 0

ans = []

def BFS() :
    d = deque()
    d.append((N, 0))
    
    while len(d) != 0 :
        print(d)
        now = d.popleft()
        where = now[0]
        time = now[1]

        if len(ans) != 0 :
            if time > ans[0] : continue
        if where == K : 
            ans.append(time)
            continue
        if where < K :
            if 2*where < 100001 and used_lst[2*where] >= time +1 : 
                d.append((2*where, time + 1))
                used_lst[2*where] = time + 1
            if where+1 < 100001 and used_lst[where+1] >= time +1  : 
                d.append((where+1, time + 1))
                used_lst[where+1] = time + 1
        if where-1 >= 0 and used_lst[where-1] >= time + 1  : 
            d.append((where-1, time + 1))
            used_lst[where-1] = time + 1

        
if N > K : print (N - K)
else :
    BFS()
    print(ans[0])
    print(len(ans))