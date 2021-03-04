import sys
input = sys.stdin.readline

N = int(input())
lst = list(map(int, input().split()))
ans = 0
lst.sort()
#print(lst)
for i in range (len(lst)) :
    for j in range (i+1) :
        ans += lst[j]
print(ans)