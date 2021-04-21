import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
N = int(input())
for i in range (1, N+1) :
    s = i
    for j in str(i) :
        s += int(j)
    #print(s)
    if s == N :
        print(i)
        break
else : print(0)