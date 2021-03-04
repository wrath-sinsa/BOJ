import sys
input = sys.stdin.readline

N, X = map(int, input().split())
value = list()
for i in range (N) :
    value.append(int(input()))
value.sort()
# 자르는 것을 a 길이 라고 하자.
ans = 0
l, r = 1, value[N-1]
while l <= r : 
    tmp = 0
    a = (l + r) // 2
    #print(a)
    for i in range (N) :
        tmp += value[i] // a
    if tmp >= X :
        if ans < a : ans = a
        l = a + 1
    else : r = a - 1
print (ans)