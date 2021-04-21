import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
#N = int(input())
N, M = map(int,input().split())
lst = list(map(int, input().split()))

s = [0] * (N+1)
for i in range (1,N+1) : # N
    s[i] = (s[i-1] + lst[i-1]) % M

m = [0] * (M)
for i in range (N+1) :
    m[s[i]] += 1

#print(s)
#print(m)

S = 0
for i in range (M) :
    a = m[i]
    S += a * (a-1) // 2 # aC2
print(S)