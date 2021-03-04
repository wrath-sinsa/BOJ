import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())

used_lst = [0] * 100001
used_lst[N] = 1

ans = []

def BFS() :
    d = deque()
    d.append((N, 0))

    while len(d) != 0 :
        #print(d)
        now = d.popleft()
        where = now[0]
        time = now[1]

        if where == K : return time

        if 2*where < 100001 and used_lst[2*where] == 0 :
            tmp = where
            while 2*tmp < 100001 and used_lst[2*tmp] == 0 :
                d.append([2*tmp, time])
                used_lst[2*tmp] = 1
                tmp *= 2
        if where+1 < 100001 and used_lst[where+1] == 0 : 
            d.append([where+1, time + 1])
            used_lst[where+1] = 1
        if where-1 >= 0 and used_lst[where-1] == 0 : 
            d.append([where-1, time + 1])
            used_lst[where-1] = 1

if N > K : print (N - K)
else :
    print(BFS())
    