import sys
import heapq
import math
sys.setrecursionlimit(100000)
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def TreeDFS(curr) :
    for nxt in Tree[curr] :
        if par[nxt] == -1 :
            par[nxt] = curr
            TreeDFS(nxt)
# __main__

N = int(input())
#N, M = map(int,input().split())
Tree = [list() for i in range(N+1)]
for i in range (N-1) :
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

par = [-1] * (N+1)
par[1] = 1
TreeDFS(1)
print(*par[2:])