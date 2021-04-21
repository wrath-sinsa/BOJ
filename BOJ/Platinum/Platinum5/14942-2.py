import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def TreeDFS(curr) :
    for nxt, dis in graph[curr] :
        if parse_r[nxt][0] == 0  :
            parse_r[nxt][0] = curr
            parse_d[nxt][0] = dis
            TreeDFS(nxt)

# __main__
N = int(input())
ant = list()
for i in range (N) :
    ant.append(int(input()))

graph = [list() for i in range (N+1)]
parse_r = [[0]*(19) for i in range (N+1)]
parse_d = [[0]*(19) for i in range (N+1)]
for i in range (N-1) :
    tmp = list(map(int, input().split()))
    graph[tmp[0]].append((tmp[1], tmp[2]))
    graph[tmp[1]].append((tmp[0], tmp[2]))
#print(graph)

parse_r[1][0] = -1
TreeDFS(1)
#print(parse_r, parse_d)
# memo
for j in range (1, 19) :
    for i in range (1, N+1):
        if parse_r[i][j-1] > 0 :
            parse_r[i][j] = parse_r[ parse_r[i][j-1] ][j-1]
            parse_d[i][j] = parse_d[ parse_r[i][j-1] ][j-1] + parse_d[i][j-1]
#print(parse_r, parse_d)

for i in range (N) :
    hp = ant[i]
    x = i+1
    for i in range (19-1, -1, -1) :
        if parse_r[x][i] > 0 and hp >= parse_d[x][i] :
                hp -= parse_d[x][i]
                x = parse_r[x][i]
    print(x)

# 1에서 2가는것과 2에서 1가는것 둘다 저장해서 dfs를 돌려야할듯