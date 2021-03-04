import sys
input = sys.stdin.readline

N = int(input())
lst = list()
for i in range (N) :
    lst.append(int(input()))
## 산술 평균 O(N)
s = sum(lst)
a = s // N
b = s / N
if (b - a < 0.5 ) :
    print(a)
else : print(a +1)

## 중앙값 O(N)
lst.sort()
print(lst[N//2])

## 최빈값 O(N)
minimum = 0
A = [[0] * 4001 for i in range (2)]
for i in lst :
    if i >= 0 :
        A[0][i] += 1
    else : # i < 0
        A[1][i*-1] += 1
maximum = max(max(A[0]), max(A[1]))
cnt = []
for i in range (2) :
    for j in range (4001) :
        if A[i][j] == maximum :
            if i == 0 :
                cnt.append(j)
            else :
                cnt.append(-j)
if len(cnt) > 1 : print(sorted(cnt)[1])
else : print(cnt[0])

# 범위 O(1)
print(lst[N-1] - lst[0])
