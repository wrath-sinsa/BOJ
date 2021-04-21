import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def struct() : # N
    for i in range (size-1, 0,-1) :
        lst[i] = lst[2*i] + lst[2*i+1]

def update(i, val) :
    idx = (i-1) + size
    lst[idx] = val
    while idx > 0 :
        idx //= 2
        lst[idx] = lst[2*idx] + lst[2*idx+1]

def segment_sum(L, R, idx ,l, r) :
    #print (L, R, idx, l, r)
    if L <= l and r <= R : return lst[idx]
    elif r < L or R < l : return 0
    mid = (l+r) //2
    a = segment_sum(L, R, idx*2, l, mid)
    b = segment_sum(L, R, idx*2+1, mid+1, r)
    return a + b
# __main__
# N = int(input())
N, M, K = map(int,input().split())

exp = math.ceil(math.log(N, 2))
size = int(2 ** exp) 
#print(exp)
 
lst = [0] * (size*2) # N ==4 : exp = 2 : 9
# for i in range (int(2**exp), int(2**(exp+1)) : # 4, 8 

for i in range (size, size+N) :
    lst[i] = int(input())
#print(lst)

struct()
#print(lst)

for i in range (M+K) :
    a, b, c = map(int, input().split())
    if a == 1 :
        update(b, c)
    elif a == 2 :
        print(segment_sum(b-1+size, c-1+size, 1, size, 2*size-1))