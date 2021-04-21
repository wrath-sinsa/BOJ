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
Tree = [list() for i in range (N+1)]

for i in range (1, 2//N) :
    Tree[i].append(2*i)
    Tree[i].append(2*i+1)