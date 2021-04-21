import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__
N = int(input())
ant = list()
for i in range (N) :
    ant.append(int(input()))

lst = [[[0, 0]]*(19) for i in range (N+1)]
for i in range (N-1) :
    tmp = list(map(int, input().split()))
    lst[tmp[1]][0] = [tmp[0], tmp[2]]
#print(lst)

for j in range (1, 19) :
    for i in range (1, N+1):
        lst[i][j] = [lst[ lst[i][j-1][0] ][j-1][0], lst[ lst[i][j-1][0] ][j-1][1] + lst[i][j-1][1]]
print(lst)

for i in range (N) :
    hp = ant[i]
    x = i+1
    exp = 19
    while (exp) :
        exp -= 1
        if lst[x][exp][0] != 0 :
            if hp >= lst[x][exp][1] :
                hp -= lst[x][exp][1]
                x = lst[x][exp][0]
    print(x)