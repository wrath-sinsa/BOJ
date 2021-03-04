import sys
input = sys.stdin.readline

M, N = map(int,input().split())
lst = list(range(N+1))
lst[1] = 0
i = 2 
while i <= int(N ** 0.5) :
    j = 2 
    if lst[i] != 0 :
        while i * j <= N :
            lst[i * j] = 0
            j += 1
    i += 1
for i in range (M, N+1) :
    if (lst[i]) : print(lst[i])