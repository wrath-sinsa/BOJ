import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
INF = 1000000001
N = int(input())
#N, M = map(int,input().split())

lst = list()
for i in range (N) :
    tmp = tuple(map(int, input().split()))
    lst.append(tmp)
lst.sort()
#print(lst)

ans = 0
l = -INF
r = -INF


for i in range (N) :
    if r < lst[i][0] : # 합칠 수 없으면
        # print(l, r)
        ans += r-l
        l = lst[i][0]
        r = lst[i][1]
        # print(l, r)
    else : # 합칠 수 있으면
        r = max(r, lst[i][1])
ans += r-l
print(ans)

