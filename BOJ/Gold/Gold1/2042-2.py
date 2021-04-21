import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def tree_sum(idx) :
    ans = 0
    while (idx > 0) :
        ans += tree[idx]
        idx -= (idx & -idx)
    return ans

def update(idx, diff) :
    while (idx < size+1) :
        tree[idx] += diff
        print (idx, idx & -idx, bin(idx)[2:], bin(idx&-idx)[2:], tree)
        idx += (idx & -idx)

# __main__
#N = int(input())
N, M, K = map(int,input().split())

exp = math.ceil(math.sqrt(N))
size = 2 ** exp
tree = [0] * (size+1)

lst = [0] * (size + 1)
for i in range (1,N+1) :
    lst[i] = int(input())
    update(i, lst[i])

for i in range (M+K) :
    a, b, c = map(int, input().split())
    if a == 1 :
        diff = c - lst[b]
        lst[b] = c
        update(b, diff)
    elif a == 2:
        print(tree_sum(c) - tree_sum(b-1))