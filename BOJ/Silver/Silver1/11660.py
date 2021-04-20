import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
N, M = map(int,input().split())
lst = list()
for i in range (N) :
    lst.append(list(map(int,input().split())))
#print(lst)
s = [[0]* (N+1) for i in range (N+1)]
for i in range (1, N+1) : 
    for j in range (1, N+1) :
        s[i][j] = s[i][j-1] + s[i-1][j] - s[i-1][j-1] + lst[i-1][j-1]
#print(s)

for i in range (M) :
    y1, x1, y2, x2 = map(int,input().split())
    #print(s[y2][x2] , s[y1-1][x2] , s[y2][x1-1] , s[y1-1][x1-1])
    print(s[y2][x2] - s[y1-1][x2] - s[y2][x1-1] + s[y1-1][x1-1])