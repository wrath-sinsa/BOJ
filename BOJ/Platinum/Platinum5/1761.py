import sys
import heapq
import math
sys.setrecursionlimit(100000)
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def TreeDFS(curr) :
    for nxt, cost in Tree[curr] :
        if depth[nxt] == -1 :
            parse[nxt][0] = curr
            parse_c[nxt][0] = cost
            depth[nxt] = depth[curr] + 1
            TreeDFS(nxt)

def LCA(u, v) :
    ans = 0
    if depth[u] < depth[v] : u, v = v, u
    
    diff = depth[u] - depth[v] 
    tmp = 0
    while diff : # log N
        if diff % 2 == 1 :
            ans += parse_c[u][tmp]
            u = parse[u][tmp]
        diff //= 2 
        tmp += 1

    if u != v :
        for ex in range (Exp-1, -1 , -1) : # log N
            if parse[u][ex] != parse[v][ex] :
                ans += parse_c[u][ex]
                ans += parse_c[v][ex]
                u = parse[u][ex]
                v = parse[v][ex]
        ans += parse_c[u][0]
        ans += parse_c[v][0]
        u = parse[u][0]

    return ans
# __main__

N = int(input())
#N, M = map(int,input().split())
Tree = [list() for i in range (N+1)]
for i in range (N-1) :
    a, b, c = map(int, input().split())
    Tree[a].append((b,c))
    Tree[b].append((a,c))

depth = [-1]*(N+1)
depth[1] = 0

Exp = math.ceil(math.log2(N))
parse = [[0]*Exp for i in range (N+1)]
parse_c = [[0]*Exp for i in range (N+1)]
TreeDFS(1)

for j in range (1, Exp) : # logN
    for i in range (1, N+1) : # N
        parse[i][j] = parse[parse[i][j-1]][j-1]
        parse_c[i][j] = parse_c[parse[i][j-1]][j-1] + parse_c[i][j-1]

#print(parse, parse_c)

M = int(input())

for i in range (M) :
    a, b = map(int, input().split())

    print(LCA(a, b))


# 1. LCA 구할때 거리구하기
# 2. u부터 route 거리 + v 부터 route 거리 - 2 * LCA(u,v)부터 route 거리