import sys
input = sys.stdin.readline

N = int(input())
sequence = list(map(int, input().split()))
ans = [0] * N
lst = []
lst.append((sequence[0], 0))
i = 1
j = 0
while i < N :
    while j >= 0 and lst[j][0] < sequence[i] : # 스택보다 원소가 큰경우
        # ans에 넣어주기
        ans[lst[j][1]] = sequence[i]
        lst.pop()
        j -= 1
    lst.append((sequence[i], i))
    j += 1
    i += 1
for i in range (len(lst)) :
    ans[lst[i][1]] = -1
for i in range (N) : print(ans[i], end=" ")

