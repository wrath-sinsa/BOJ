n, m = map(int ,input().split())
lst = [[0]*101 for i in range (101) ]

def Combination(N, M) :
    if 2*M > N : 
        M = N - M
    if M == 0 :
        lst[N][M] = 1
        return 1
    if M == N :
        lst[N][M] = 1
        return 1
    if lst[N][M] != 0 :
        return lst[N][M]
    lst[N][M] = Combination(N-1, M-1) + Combination(N-1, M)
    return lst[N][M]
print(Combination(n,m))
