import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

# __main__
N = int(input())
M = int(input())
lst = [[sys.maxsize]*(N+1) for i in range (N+1)]
for i in range (M) :
    tmp = list(map(int, input().split()))
    if lst[tmp[0]][tmp[1]] > tmp[2] :
        lst[tmp[0]][tmp[1]] = tmp[2]
for i in range (1,N+1) :
    lst[i][i] = 0
# for i in lst :
#     for j in i :
#         print(j, end = " ")
#     print("")

#ployd-warshall
for k in range (1,N+1) :
    for i in range (1,N+1) :
        for j in range (1,N+1) :
            lst[i][j] = min(lst[i][j], lst[i][k] + lst[k][j])

for i in range (1, len(lst)) :
    for j in range (1, len(lst)) :
        if lst[i][j] == sys.maxsize : print(0, end = " ")
        else : print(lst[i][j], end = " ")
    print("")