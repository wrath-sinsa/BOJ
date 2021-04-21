import sys
import heapq
import math
from collections import deque
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

N = int(input())
#N, M = map(int,input().split())
M = int(input())

graph = [list() for i in range (N+1)]

for i in range (M) :
    a, b, c = map(int, input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))

for i in range (1, N+1) :
    heapq.heapify(graph[i])

INF = 1000 * 10000
used = [0] * (N+1)

lst = list()
lst.append(1)
used[1] = 1

ans = 0
for i in range (1, N+1 -1):
    x = lst.pop()
    while (lst):
        z, y = pop(graph[x])
        if (used[y] == 0) :
            ans += z
            used[y] = 1
            lst.append(y)
            break
        pop(lst)

print(ans)

# 1에서 최솟값(2)을 뽑은 뒤
# 2를 둘러봤을때 최솟값 설정이 불가능하다면
# 1로 돌아가야하는데 안됨.

# 그냥 lst에 넣어놓고 최솟값만 계속 뽑아내는 게 쉬울듯
