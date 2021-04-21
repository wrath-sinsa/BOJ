import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

#N = int(input())
N, M = map(int,input().split())
lst = [0] * (M-N+1)
ans = M-N+1
i = 2
while i * i <= M : # M ** 0.5 ~= 1000,000+1
    a = math.ceil(N / (i * i))
    #print(a)
    while a * (i*i) <= M :
        if lst[a*(i*i)-N] == 0 :
            lst[a*(i*i)-N] = 1
            ans -= 1
        a += 1
    i += 1
print(ans)
