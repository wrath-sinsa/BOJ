T = int(input())
for i in range (T) :
    N, M = map(int, input().split())
    s1 = 1 
    s2 = 1
    if N > M // 2 :
        N = M - N
    for i in range (N) :
        s1 *= M - i
    for j in range (N) :
        s2 *= N - j
    print (s1 // s2)
    