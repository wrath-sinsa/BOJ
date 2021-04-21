import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

# __main__
M = int(input())

lst = [[0] * (19) for i in range (M+1)]
f = list(map(int, input().split()))
for i in range (1, M+1) :
    lst[i][0] = f[i-1]

# 배열 초기화
for i in range (1, 19) :
    for j in range (1, M+1) :
        lst[j][i] = lst[ lst[j][i-1] ][i-1]
#print(lst)

# 쿼리
Q = int(input())
for i in range (Q) :
    tmp = list(map(int, input().split()))
    exp = 0
    while tmp[0] > 0 : # 지수만큼 반복
        if tmp[0] % 2 == 1 :
            tmp[1] = lst[ tmp[1] ][exp]
        tmp[0] //= 2
        exp += 1
        #print(tmp[0], tmp[1])
    print(tmp[1])