import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))
def update(idx) :
    idx += SIZE
    while idx > 0 :
        segment[idx] += 1
        idx //= 2

def seg(s, e) :
    return seg_sum(s+SIZE, 2*SIZE-1, 1, SIZE, 2*SIZE-1)

def seg_sum(s, e, node, ns, ne) :
    if e < ns or s > ne : return 0
    if s <= ns and ne <= e : return segment[node]
    mid = (ns + ne) // 2
    return seg_sum(s, e, node*2, ns, mid) + seg_sum(s, e, node*2+1, mid+1, ne)


# __main__
T = int(input())
for i in range (T) :

    N = int(input())
#N, M = map(int,input().split())
    exp = math.ceil(math.log2(N))
    SIZE = 2**exp
    segment = [0] * (2*SIZE)

    dot = []
    for i in range (N) :
        a, b = map(int,input().split())
        dot.append([a, b])

    # y좌표 큰순 정렬
    dot.sort(key=lambda x:x[1])
    #print(dot)

    newY = [-1] * (N)
    now = 0
    for i in range (N) :
        if i != 0 and dot[i][1] > dot[i-1][1] : now+=1
        newY[i] = now
    for i in range (N) :
        dot[i][1] = newY[i]

    dot.sort(key=lambda x:(x[0], -x[1]))
    #print(dot)

    ans = 0
    for i in range (N) :
        ans += seg(dot[i][1], SIZE)
        update(dot[i][1]) # 0~SIZE-1 값을 가지므로 idx로 활용
    print(ans)