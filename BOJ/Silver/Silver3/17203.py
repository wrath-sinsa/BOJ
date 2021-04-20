import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
N,M = map(int,input().split())
lst = list(map(int, input().split()))

s = [0] * (N+1)
for i in range (2, N+1) :
    s[i] = s[i-1] + abs(lst[i-1] - lst[i-2])
#print(s)

for i in range (M) :
    x1, x2 = map(int, input().split())
    print(s[x2]-s[x1])