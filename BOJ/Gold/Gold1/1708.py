import sys
import heapq
import math
from collections import deque
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

def CCW(a, b, c) :
    dx1, dy1 = b[0]-a[0], b[1]-a[1]
    dx2, dy2 = c[0]-a[0], c[1]-a[1]
    return dx1*dy2-dy1*dx2
N = int(input())
#N, M = map(int,input().split())
dot = list()
for i in range (N) :
    tmp = list(map(int,input().split()))
    dot.append(tmp)
dot.sort(key = lambda x:(-x[0], x[1]))
print(dot)

for i in range (1,N) :
    tdx = dot[i][0] - dot[0][0]
    tdy = dot[i][1] - dot[0][1]
    theta = tdy / (abs(tdx) + abs(tdy))
    dot[i].append(theta)

tmp = [dot[0]]
dot = sorted(dot[1:], key = lambda x : (-x[2], x[1], -x[0]))
dot = tmp + dot
print(dot)

st = deque()
st.append(0)
st.append(1)
nxt = 2
while nxt < N : # N
    while len(st) >= 2 : 
        second = st.pop()
        first = st[-1]

        if CCW(dot[first], dot[second], dot[nxt]) > 0 :
            st.append(second)
            break
    st.append(nxt)
    nxt += 1

#print(st)
print(len(st))
