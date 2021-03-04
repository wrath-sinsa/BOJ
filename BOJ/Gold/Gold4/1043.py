import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int,input().split())
d = deque()
tmp = list(map(int, input().split()))
for i in range (1, len(tmp)) :
    d.append(tmp[i])

lst = list()
for i in range (M) :
    tmp = list(map(int, input().split()))
    lst.append(tmp)

used = [0] * (M)
used2 = [0] * (N+1)
for i in range (len(d)) :
    used2[d[i]] = 1

while (len(d)) :
    chk = d.popleft()
    for i in range (M) :
        if used[i] == 0 :
            for j in range (1, lst[i][0]+1) :
                if lst[i][j] == chk :
                    used[i] = 1
                    for k in range (1, lst[i][0]+1) :
                        if used2[lst[i][k]] == 0 :
                            used2[lst[i][k]] = 1
                            d.append(lst[i][k])
                    break
    #print(d)
#print(used)
print(used.count(0))