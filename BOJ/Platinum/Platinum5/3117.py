import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
N, K, M = map(int,input().split())

start = list(map(int, input().split()))
tmp = list(map(int, input().split()))

lst = [[0]*(30) for i in range (K+1)]
for i in range (1, K+1) :
    lst[i][0] = tmp[i-1] # 첫번째 학생이 1번 봤을때 = 가장 위에 있는 동영상 번호
#print (lst)

for i in range (1, 30) :
    for j in range (1, K+1) :
        lst[j][i] = lst[ lst[j][i-1] ][i-1]
#print(lst)
for i in range (N) :
    m = M-1
    exp = 0
    x = start[i]
    while m > 0 :
        if m % 2 == 1 :
            x = lst[x][exp]
        m //= 2
        exp += 1
    print (x, end = " ")