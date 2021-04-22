N, K = map(int, input().split())

DP = [[0] * (K+1) for i in range (N+1)]


weight = [0] * (N+1)
value = [0] * (N+1)

for i in range (1, N+1) :
    a, b= map(int, input().split())
    weight[i] = a 
    value[i] = b


for i in range (1, N+1) :
    for w in range (1, K+1) : 
        if w < weight[i] : 
            DP[i][w] = DP[i-1][w]
        else :
            DP[i][w] = max(DP[i-1][w], DP[i-1][w-weight[i]]+value[i]) 

# for i in range (1, N+1) :
#     for w in range (1, K+1) :
#         print(DP[i][w] , end = " ")
#     print("")

print(DP[N][K])