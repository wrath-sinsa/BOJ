import sys
import heapq
input = sys.stdin.readline

def add(s, x) :
    s = s|1<<x 
    return s

def remove(s, x):
    s = s&~(1<<x)
    return s

def left(s) :
    s = s << 1
    if (len(bin(s)) == 23) :
        s = remove(s, 21 - 1)
    return s

def right(s) :
    s = s >> 1
    return s

# __main__
N, M = map(int,input().split())
lst = [0] * N
for i in range (M) :
    tmp = list(map(int, input().split()))
    if tmp[0] == 1 :
        lst[tmp[1]-1] = add(lst[tmp[1]-1], tmp[2]-1)
    elif tmp[0] == 2 :
        lst[tmp[1]-1] = remove(lst[tmp[1]-1], tmp[2]-1)
    elif tmp[0] == 3 :
        lst[tmp[1]-1] = left(lst[tmp[1]-1])
    elif tmp[0] == 4 :
        lst[tmp[1]-1] = right(lst[tmp[1]-1])
    # for i in lst :
    #     print(bin(i))
print(len(set(lst)))