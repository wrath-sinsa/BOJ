import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# # __main__

# N = int(input())
# N, M = map(int,input().split())

A, B, C = map(int,input().split())

def times(a, b, c):
    if b == 0 : return 1
    num = times(a, b//2, c)%c
    tmp = (num * num)%c
    if b % 2 == 1 :
        return ( tmp * (a%c) ) % c
    else :
        return tmp

print(times(A,B,C))