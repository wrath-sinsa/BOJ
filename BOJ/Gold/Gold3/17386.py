import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

def CCW(a, b, c) :
    dx1, dy1 = b[0]-a[0], b[1]-a[1]
    dx2, dy2 = c[0]-a[0], c[1]-a[1]
    
    ans = dx1*dy2-dy1*dx2
    if ans > 0 : return 1
    if ans < 0 : return -1
    # 한 직선상에 위에 있을때
    if dx1*dx1+dy1*dy1 < dx2*dx2+dy2*dy2 : return 1
    return 0

def intersect(a, b, c, d) :
    t1 = CCW(a,b,c) * CCW(a,b,d)
    t2 = CCW(c,d,a) * CCW(c,d,b)
    return int(t1 <= 0 and t2 <= 0)
#N = int(input())
#N, M = map(int,input().split())
x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())
A = [x1, y1]
B = [x2, y2]
C = [x3, y3]
D = [x4, y4]

print(intersect(A,B,C,D))