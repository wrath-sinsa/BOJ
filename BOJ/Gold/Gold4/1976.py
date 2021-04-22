import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def find(n) :
    if p[n] < 0 : return n
    p[n] = find(p[n])
    return p[n]

def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b : return
    p[b] = a 

# __main__
N = int(input()) 
M = int(input())
lst = [list(map(int,input().split())) for i in range (N)]
go = list(map(int,input().split()))
p = [-1] * N

for i in range (N) :
    for j in range (N) :
        if lst[i][j] == 1 : merge(i, j)
        
for i in range (M-1) :
    if find(go[i]-1) != find(go[i+1]-1) : # 같은 집합에 있지 않다면
        print("NO")
        break
else :
    print("YES")