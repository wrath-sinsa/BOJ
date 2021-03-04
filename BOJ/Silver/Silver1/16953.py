import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

lst = deque()


def BFS() :
    cnt = 0 
    while len(lst) != 0 :
        l = len(lst)
        for i in range (l) :
            now = lst.popleft()
            if now > B :
                continue
            if now == B : return cnt
            print(now)
            lst.append(2*now)
            lst.append(now*10+1)
        cnt += 1
    return -2
lst.append(A)
print(BFS()+1)