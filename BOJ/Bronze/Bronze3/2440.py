import sys

input = sys.stdin.readline

# __main__
N = int(input())

for i in range (N, 0, -1) :
    print ("*"*i, end="\n")