import sys
import heapq
sys.setrecursionlimit(100000)
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def dynamic(n) :
    #print(DP, n)
    if DP[n] != sys.maxsize : return DP[n]
    a = sys.maxsize
    b = sys.maxsize
    if n % 3 == 0 :
        a = dynamic(n//3) + 1
    if n % 2 == 0 :
        b = dynamic(n//2) + 1
        
    c = dynamic(n-1) + 1
    DP[n] = min([a,b,c])
    return DP[n]
# __main__
N = int(input())
DP = [sys.maxsize] * (N+1) 
DP[1] = 0
print(dynamic(N))
#print(DP)

# 1, 1, 1, 2, 3, 2,