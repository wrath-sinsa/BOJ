import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))




# __main__
N, M = map(int,input().split())
lst = list(map(int, input().split()))
#print(lst)

s = [0] * (N+1)
for i in range (1, N+1) :
    s[i] = s[i-1] + lst[i-1]
#print(s)

for i in range (M) :
    tmp = list(map(int, input().split()))
    print(s[tmp[1]] - s[tmp[0]-1])