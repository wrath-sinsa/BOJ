import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

#N = int(input())
N, E = map(int,input().split())

Graph = [list() for i in range (N+1)]
for i in range (E) :
    a, b, c = map(int,input().split())
    lst[a].append((b,c))
    lst[b].append((a,c))



v1, v2 = map(int, input().split())

