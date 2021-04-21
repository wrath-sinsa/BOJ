import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def TreeDFS(curr, dis, expense) :
    for nxt, cost in Tree[curr] :
        if dis[nxt] == -1 :
            dis[nxt] = expense + cost
            TreeDFS(nxt, dis, dis[nxt])

# __main__

V = int(input())
#N, M = map(int,input().split())
Tree = [list() for i in range (V+1)]

for i in range (V) :
    tmp = list(map(int,input().split()))
    for j in range (1, len(tmp)-1, 2) : # 4
        Tree[tmp[0]].append((tmp[j], tmp[j+1]))
#print(Tree)

dis1 = [-1] * (V+1)
dis1[1] = 0
TreeDFS(1,dis1, 0)

Max = 0
M_i = 0
for i in range (1,V+1) :
    if Max < dis1[i] :
        Max=dis1[i]
        M_i = i

dis2 = [-1] * (V+1)
dis2[M_i] = 0
TreeDFS(M_i, dis2, 0)
print(max(dis2))