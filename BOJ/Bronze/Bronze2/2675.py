import sys 

T = int(sys.stdin.readline())
for i in range (T) :
    A = list(sys.stdin.readline().split())
    for v in A[1] :
        print(v*int(A[0]), end="")
    print("")