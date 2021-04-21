import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def find(n) :
    if p[n] < 0 : return n
    p[n] = find(p[n]) 
    return p[n]

def merge(a, b) :
    a = find(a)
    b = find(b)
    if a == b: return False
    p[b] = a
    return True
# __main__
V,E = map(int,input().split())
lst = list()
for i in range (E) :
    tmp = list(map(int, input().split()))
    push(lst, (tmp[2], tmp[0], tmp[1]))

p = [-1] * (V+1)
cnt = 0
ans = 0
while (lst) :
    v, now, nxt = pop(lst)
    if(merge(now, nxt)) :
        cnt += 1
        ans += v
        if cnt == V-1 : break
print(ans)