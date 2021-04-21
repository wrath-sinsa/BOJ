import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def find(n):
    if p[n] < 0 : return n
    p[n] = find(p[n])
    return p[n]

def merge(a, b):
    a = find(a)
    b = find(b)
    if a == b :return
    if p[a] > p[b] :
        a, b = b, a
    p[a] += p[b]
    p[b] = a


# __main__
N, M, K = list(map(int, input().split()))
friend = list(map(int,input().split()))

p = [-1] * N
for i in range (M) :
    tmp = list(map(int,input().split()))
    merge(tmp[0]-1, tmp[1]-1)

ans = [sys.maxsize] * N
for i in range (N) :
    idx = find(i)
    if ans[idx] > friend[i] : ans[idx] = friend[i]

a = 0
for i in range (N) :
    if ans[i] != sys.maxsize :
        a += ans[i]
if a <= K : print(a)
else : print ("Oh no")