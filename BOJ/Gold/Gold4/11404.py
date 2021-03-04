import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

# __main__
N = int(input())
M = int(input())
MAX = 100001
lst = [[MAX]*N for i in range (N)]
for i in range (M) :
    tmp = list(map(int, input().split()))
    if lst[tmp[0]-1][tmp[1]-1] > tmp[2] :
        lst[tmp[0]-1][tmp[1]-1] = tmp[2]
for i in range (N) :
    lst[i][i] = 0
# for i in lst :
#     for j in i :
#         print(j, end = " ")
#     print("")
#ployd-warshall
for i in range (N) :
    for j in range (N) :
        if lst[i][j] != MAX :
            for k in range (N) :
                lst[k][j] = min(lst[k][j], lst[k][i] + lst[i][j])

for i in lst :
    for j in i :
        print(j, end = " ")
    print("")