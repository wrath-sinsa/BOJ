import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def dynamic(n) :
    if DP[n] != 0 : return DP[n]
    tmp = 0
    if n-1 > 0 : tmp += dynamic(n-1)
    if n-2 > 0 : tmp += dynamic(n-2)
    if n-3 > 0 : tmp += dynamic(n-3)
    DP[n] = tmp
    return DP[n]
# __main__

T = int(input())
#N, M = map(int,input().split())
DP = [0] * (12)
DP[1] = 1 # 1
DP[2] = 2 # 1 + 1 , 2
DP[3] = 4 # 1 + 1 + 1 , 2+ 1, 1 + 2, 3
for i in range (4, 12) :
    DP[i] = DP[i-1] + DP[i-2] + DP[i-3] 
#print(DP)

for i in range (T) :
    N = int(input())
    print(DP[N])
    #print(dynamic(N))
#print(DP)