import sys
import heapq
import math
sys.setrecursionlimit(30000)
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def TreeDFS(curr) :
    for nxt in graph[curr] :
        if depth[nxt] == -1 :
            parse[nxt][0] = curr 
            depth[nxt] = depth[curr]+1
            TreeDFS(nxt)

# __main__

N = int(input())
#N, M = map(int,input().split())
graph = [list() for i in range (N+1)]
for i in range (N-1) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 깊이를 정해주는 리스트
depth = [-1] * (N+1)
depth[1] = 0 

#희소 행렬
exp = math.ceil(math.log2(N))
parse = [[0]*exp for i in range (N+1)]

# Tree에서 원소의 깊이를 지정
TreeDFS(1)

#희소 행렬을 채움
for j in range (1,exp) :
    for i in range (1, N+1) :
        parse[i][j] = parse[parse[i][j-1]][j-1]

# 쿼리 개수
M = int(input())
for i in range (M) :
    u, v = map(int, input().split())
    
    if depth[u] < depth[v] : u, v= v, u
    diff = depth[u] - depth[v]

    tmp = 0
    while diff != 0 : #logN
        if diff % 2 == 1 :
            u = parse[u][tmp]
        diff //= 2
        tmp += 1 

    if u != v :
        for ex in range (exp-1, -1, -1) : # logN
            if parse[u][ex] != parse[v][ex] :
                u = parse[u][ex]
                v = parse[v][ex]
                
        u = parse[u][0]
    print(u)