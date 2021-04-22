import sys
import heapq
import math
sys.setrecursionlimit(30000)
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def DFS(dis, cost, now) :
    for nxt, exp in Tree[now] :
        if dis[nxt] == -1 :
            dis[nxt] = cost + exp
            DFS(dis, cost+exp, nxt)
# __main__

N = int(input())
#N, M = map(int,input().split())

Tree = [list() for i in range (N+1)]
for i in range (N-1) :
    a, b, c = map(int, input().split()) 
    Tree[a].append((b, c))
    Tree[b].append((a, c))
dis1 = [-1] * (N+1)
dis1[1] = 0
DFS(dis1, 0, 1)

M_i = 0
MAX = 0
for i in range (1, N+1) :
    if dis1[i] > MAX :
        MAX = dis1[i]
        M_i = i

dis2 = [-1] * (N+1)
dis2[M_i] = 0
DFS(dis2, 0, M_i)

print(max(dis2))