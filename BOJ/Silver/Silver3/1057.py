def round(K, I) : 
    cnt_k = 0
    cnt_i = 0
    tmp_K = K
    tmp_I = I
    while tmp_K > 1 :
        tmp_K //= 2
        cnt_k +=1
    while tmp_I > 1 :
        tmp_I //= 2
        cnt_i += 1
    if cnt_k != cnt_i :
        print(max([cnt_i, cnt_k]) + 1)
    else : # 같은 경우
        if cnt_i == 0 and cnt_k == 0 :
            print(1)
            return
        K -= 2 ** cnt_k
        I -= 2 ** cnt_i
        round(K, I)

N, K, I = map(int, input().split())
K -= 1 # 계산 편의
I -= 1 # 계산 편의
round(K,I)

