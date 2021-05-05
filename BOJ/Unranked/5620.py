import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
INF = 900000000

def solve(l, r) :
    #print(l, r)
    if l == r : return INF
    m = (l + r)//2
    dis_min = min(solve(l, m), solve(m+1, r))
    #print(l, r, dis_min)

    # 살펴볼 점 리스트
    lst = list()

    # l부터 m까지
    for i in range (m,l-1,-1) :
        if (dot[i][0] - dot[m][0]) ** 2 < dis_min :
            lst.append(dot[i])
        else : break
    # m+1부터 r까지
    for i in range (m+1, r+1) :
        if (dot[i][0] - dot[m][0]) ** 2 < dis_min :
            lst.append(dot[i])
        else : break

    lst.sort(key=lambda x : x[1])
    for i in range (len(lst)-1) :
        for j in range (i+1, len(lst)) :
            if (lst[j][1]-lst[i][1])**2 < dis_min :
                dis = (lst[i][0]-lst[j][0])**2+(lst[i][1]-lst[j][1])**2
                dis_min = min(dis, dis_min)
            else : break
    
    #print(l, r, dis_min)
    return dis_min

N = int(input())
#N, M = map(int,input().split())
dot = list()
for i in range (N) :
    a, b = map(int, input().split())
    dot.append((a,b))
dot.sort()

#print(*dot)

print(solve(0, N-1))