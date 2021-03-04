import sys

input = sys.stdin.readline

# __main__
N = int(input())

for i in range (1,2*N) :
    if i <= N :
        print(" "*(N-i), end="")
        print ("*"*(2*i-1), end="\n")
    else :
        print(" "*(i-N), end="")
        print ("*"*(2*(2*N-i)-1), end="\n")

# for i in range (1,N+1) :
#     print(" "*(N-i), end="")
#     print ("*"*(2*i-1), end="\n")
# for i in range (N-1,0,-1) :
#     print(" "*(N-i), end="")
#     print ("*"*(2*i-1), end="\n")