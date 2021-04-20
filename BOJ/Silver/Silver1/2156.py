import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

N = int(input())
#N, M = map(int,input().split())
lst = [0] * (10000+1)
for i in range (1, N+1) :
    lst[i] = int(input())

DP = [0] * (10000+1)
DP[1] = lst[1]
DP[2] = lst[1] + lst[2]
DP[3] = max([DP[2], DP[1] + lst[3], DP[0] + lst[2] + lst[3]])
DP[4] = max([DP[2]+lst[4], DP[1]+lst[3]+lst[4], lst[2]+lst[3]])
for i in range (5, N+1) :
    DP[i] = max(DP[i-2], DP[i-3]+lst[i-1]) + lst[i]
    DP[i] = max(DP[i], DP[i-1])

print(DP[N])