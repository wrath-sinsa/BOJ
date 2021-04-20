N = int(input())

DP = [0] * (1000+1)
DP[1] = 1 # 1
DP[2] = 3 # 11, 2, 2
DP[3] = 5 # 111,21,21,12,12
for i in range (4, N+1) :
    DP[i] = (DP[i-1] + 2*DP[i-2]) % 10007 

print(DP[N])