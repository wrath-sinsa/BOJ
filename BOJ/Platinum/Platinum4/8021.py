import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))
def LCA(u, v) :
    s = 0

    if depth[u] < depth[v] : u, v = v, u
    
    diff = depth[u] - depth[v] 
    
    tmp = 0
    while diff:
        if diff % 2 == 1 :
            s += 2 ** tmp
            u = parse[u][tmp]
        tmp += 1 
        diff //= 2

    if u != v :
        for ex in range (Exp-1, -1, -1) :
            if parse[u][ex] != parse[v][ex] :
                s += 2 * 2 ** ex
                u = parse[u][ex]
                v = parse[v][ex]
        s += 2
        u = parse[u][0]
        v = parse[v][0]
    return s


def TreeDFS(curr) :
    for nxt in Tree[curr] :
        if depth[nxt] == -1 :
            parse[nxt][0] = curr
            depth[nxt] = depth[curr] + 1
            TreeDFS(nxt)
# __main__

N = int(input())
#N, M = map(int,input().split())
Tree = [list() for i in range (N+1)]
for i in range (N-1) :
    a, b = map(int, input().split())
    Tree[a].append(b)
    Tree[b].append(a)

depth = [-1] * (N+1)
depth[1] = 0

Exp = math.ceil(math.log2(N))
parse = [[0]*Exp for i in range (N+1)]

TreeDFS(1)

for j in range (1, Exp) :
    for i in range (1, N+1) :
        parse[i][j] = parse[parse[i][j-1]][j-1]

M = int(input())

ans = 0
pre = 0
for i in range (M) :
    nxt = int(input())
    if pre : ans += LCA(pre, nxt)
    pre = nxt
    #print ("ans = ",ans)
print(ans)