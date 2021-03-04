import sys

N = sys.stdin.readline()[:-1]
while N != "0" :
    if N == "".join(reversed(N)) :
        print("yes")
    else : print("no")
    N = sys.stdin.readline()[:-1]