

N = int (input())
DP = [0] * (1001)
DP[1] = 1 # 1
DP[2] = 2 # 1 + 1
DP[3] = 3 # 1 + 2
DP[4] = 5 # 1 + 3 + 1 # 1 : DP[3] + 2 : DP[2]
DP[5] = 8 # 1 + 4 + 3 # 1 : DP[4] + 2 : DP[3]

for i in range (6,1001) :
    DP[i] = (DP[i-1] + DP[i-2])%10007

print (DP[N])
