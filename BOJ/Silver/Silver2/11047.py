import sys
input = sys.stdin.readline

# __main__
N, K = map(int, input().split())
coin = list()
for i in range (N) : 
    coin.append(int(input()))

coin.sort(reverse=True)
#print(coin)
ans = 0
for i in range (N) :
    ans += K // coin[i]
    K -= coin[i] * (K // coin[i])
print(ans)