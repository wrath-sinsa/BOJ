import sys

N = int(sys.stdin.readline())
lstN = list(map(int, sys.stdin.readline()[:-1].split()))
M = int(sys.stdin.readline())
lstM = list(map(int, sys.stdin.readline()[:-1].split()))
for i in range (M) :
    if lstM[i] in lstN :
        print (1)
    else :
        print (0)