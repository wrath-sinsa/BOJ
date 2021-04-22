import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

def find(n):
    if uf[n] < 0 : return n
    uf[n] = find(uf[n])
    return uf[n] 

def union(a, b) :
    a = find(a)
    b = find(b)
    if a == b : return False
    uf[a] += uf[b] # 집합 사이즈
    uf[b] = a
    return True

N = int(input())
#N, M = map(int,input().split())
M = int(input())

edge = list() # hq
for i in range (M) :
    a, b, c = map(int, input().split())
    push(edge, (c,a,b))

uf = [-1] * (N+1)

ans = 0 
cnt = 0
for i in range (M) :
    c, a, b = pop(edge)
    if (union(a, b)) :
        ans += c
        #print (a,b,ans)
        cnt += 1 
        if cnt == N-1 :
            break
#print(uf)
print(ans)