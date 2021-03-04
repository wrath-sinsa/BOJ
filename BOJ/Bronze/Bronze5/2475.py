import sys

s = 0
N = "".join(sys.stdin.readline().split())
for i in N :
    s += int(i) ** 2
print (s % 10)