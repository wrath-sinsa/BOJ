import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
moduler = 1000000007
# list(map(int,input().split()))

def times(l, r, idx, left, right) :
    #print(l, r, idx, left, right)
    if l <= left and right <= r : return lst[idx]
    if right < l or left > r : return 1
    return (times(l, r, idx * 2, left, (left+right)//2) * times(l, r, idx * 2 + 1, (left+right)//2+1, right))%moduler

def update(idx, rep) : # logN
    lst[idx] = rep
    while idx > 1 :
        if idx %2 == 0 :
            lst[idx//2] = (lst[idx+1] * lst[idx])%moduler
        else :
            lst[idx//2] = (lst[idx] * lst[idx-1])%moduler
        idx //= 2

def struct() : # N
    for i in range (size-1, 0, -1) :
        lst[i] = (lst[2*i] * lst[2*i+1])%moduler

# __main__
# N = int(input())
N, M, K = map(int,input().split())

exp = math.ceil(math.log2(N)) # N =5 일때 exp = 3
size = 2 ** exp # size = 8
lst = [1] * size * 2
for i in range(size, N + size) :
    lst[i] = int(input())
struct()
#print(lst)

for i in range(M+K) :
    a, b, c = map(int , input().split())
    if a == 1 :
        update(b + size-1, c)
        #print(lst)
    elif a == 2 :
        print(int(times(size-1+b, size-1+c, 1, size, size * 2 -1)))