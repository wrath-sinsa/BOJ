
N = int(input())

def dynamic(n) :
    if DP[n] : return DP[n]



lst = [0] + list(map(int,input().split()))
lst.extend([0,0,0,0])
print(lst)
DP = [0] * ( N+1) 
DP[1] = lst[1]
DP[2] = max(DP[1], DP[1] + lst[2])
DP[3] = max(DP[2], DP[2] + lst[3])
dynamic(N)

for i in range (4, N+1) :
    if DP[i-1] < 0 :
    DP[i] = 

print(DP)
print(DP[N])



