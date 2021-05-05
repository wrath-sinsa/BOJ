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
graphA = [list() for i in range (26)]
grapha = [list() for i in range (26)]
for i in range (N) :
    a, b, c = map(str, input().split())
    if ord("A") <= ord(a) <= ord("Z") :
        graphA.append((b, c))
    else :
        grapha.append((b, c))

