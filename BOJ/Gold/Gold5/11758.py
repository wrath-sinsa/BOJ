import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

#N = int(input())
#N, M = map(int,input().split())

def CCW(a, b, c) :
    return (b[0]-a[0])*(c[1]-a[1])-(b[1]-a[1])*(c[0]-a[0])
# dx1*dy2-dy1*dx2 = 0
# dy2/dx2-dy1/dx1 과 동일

lst = list()
for i in range (3) :
    lst.append(list(map(int,input().split())))

ccw = CCW(lst[0], lst[1],lst[2])
ans = 0
if ccw > 0 : ans = 1
elif ccw < 0 : ans = -1
print(ans)