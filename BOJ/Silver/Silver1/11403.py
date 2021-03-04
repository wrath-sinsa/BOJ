import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

# __main__
N = int(input())
lst = []
for i in range (N) :
    tmp = list(map(int, input().split()))
    lst.append(tmp)
#print(lst)

for i in range(N):
    for j in range(N):
        if lst[i][j] != 0:
            for k in range(N):
                if lst[k][i] == 1 and lst[i][j] == 1 :
                    lst[k][j] = 1
for i in lst :
    for j in i :
        print (j, end=" ")
    print("")