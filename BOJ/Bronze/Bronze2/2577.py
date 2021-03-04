import sys
input = sys.stdin.readline

A = int(input())
B = int(input())
C = int(input())

ans = map(int, str(A*B*C))
lst = [0] * 10
for i in ans :
    lst[i] += 1
for i in lst :
    print (i, end="\n")
