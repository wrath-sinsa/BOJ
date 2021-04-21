import sys
import heapq
sys.setrecursionlimit(100000)
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def TreeDFS(curr) : # M
    for nxt in graph[curr] :
        if depth[nxt] == -1: # 얕은 깊이부터 지정.
            parse[nxt][0] = curr # 1 > 2 일경우 2에서 한칸 갈경우 1
            depth[nxt] = depth[curr] + 1 # 깊이는 한칸 증가
            TreeDFS(nxt) # 다음 DFS 진행

# __main__
N = int(input())
graph = [list() for i in range (N+1)]
for i in range (N-1) :
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append(tmp[1])
    graph[tmp[1]].append(tmp[0])

# 깊이를 판단하는 리스트, 희소행렬 초기화
parse = [[0] *(17) for i in range (N+1)]
depth = [-1] * (N+1)
depth[1] = 0
TreeDFS(1) # 루트부터 시작
#print(parse, depth)

# 희소행렬 채우기
for j in range (1, 17) :
    for i in range (1, N+1) :
        parse[i][j] = parse[ parse[i][j-1] ][j-1]
#print(parse, depth)

# Q 쿼리 입력
M = int(input())
for i in range (M) :
    tmp = list(map(int, input().split()))

    u, v = tmp[0], tmp[1]
    if depth[u] < depth[v] : u,v = v,u # u가 더 깊이가 깊은 곳
    #print(u, v, depth[u], depth[v])
    diff = depth[u] - depth[v]
    exp = 0
    while (diff > 0) :
        if diff % 2 == 1:
            u = parse[u][exp]
        #print (u)
        diff //= 2
        exp += 1
    #print(u, v, depth[u], depth[v])
    
    if u != v :
        for ex in range (17-1, -1, -1) : # 16 ~ 0
            #print(parse[u][ex], parse[v][ex])
            if parse[u][ex] != parse[v][ex]:
                u = parse[u][ex]
                v = parse[v][ex]
            #print (ex, u,v)
        u = parse[u][0]
    print(u)