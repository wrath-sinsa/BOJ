import sys
input = sys.stdin.readline

# __main__
N = int(input())
coin = [500, 100, 50, 10, 5, 1]
N = 1000 - N
ans = 0
for i in range (6) :
    ans += N // coin[i]
    N -= coin[i] * (N // coin[i])
print (ans) 