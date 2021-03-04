import sys

N = int(sys.stdin.readline())
for i in range (1, 9+1) :
    print("%d * %d = %d" %(N, i, N*i))