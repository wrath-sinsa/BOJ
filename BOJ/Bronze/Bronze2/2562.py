import sys

maximum = 0
for i in range (9) :
    N = int(sys.stdin.readline())
    if N > maximum :
        maximum = N
        idx = i+1
print(maximum, idx)