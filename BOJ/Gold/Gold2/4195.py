import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def find(n) :
    if p[n] < 0 : return n
    p[n] = find(p[n])
    return p[n]

def union(a, b) :
    a = find(a)
    b = find(b)
    if a == b : return
    if a > b :
        a, b = b, a
    p[a] += p[b]
    p[b] = a

# __main__
T = int(input())


for _ in range (T) :
    F = int(input())
    p = [-1] * 200001
    f_lst = dict()
    idx = 0
    for i in range (F) :
        tmp = input().split()
        if tmp[0] not in f_lst.keys() : # O(F)
            f_lst[tmp[0]] = idx
            idx += 1
        if tmp[1] not in f_lst.keys() : # O(F)
            f_lst[tmp[1]] = idx
            idx += 1

        union(f_lst.get(tmp[0]),f_lst.get(tmp[1]) )
        #print(f_lst, p)
        print(abs( p[find( f_lst.get(tmp[0]) )] ))