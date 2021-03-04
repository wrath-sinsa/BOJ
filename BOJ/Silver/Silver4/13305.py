import sys
input = sys.stdin.readline

N = int(input())
road = list(map(int,input().split()))
oil = list(map(int, input().split()))
minimum = 10000000001
s = 0
for i in range (N-1) :
    tmp = oil[i]
    if tmp < minimum : 
        minimum = tmp
    s += minimum * road[i]
print(s)