# 64칸
# 처음판정했을때 B,W,W,B,W,B,W,B이면 6번 고쳐야 하므로
# >> 그 절반이 넘어가면 거꾸로 해주기
# 48칸 색칠이면 64 - 48 = 16칸 색칠 하는것으로

# 논리
# 8개 셀때마다 그 값을 리스트에 넣어서?
# 리스트가 8개 모이면 sum을 하고?
# 다음거 넣을때 첫번째꺼를 지우고?

# 1. 체스판을 8개씩 묶어서 모든 리스트를 만든다. 세로로 모두 만들 예정
# 2. 한칸 내려갈때 빼줄 리스트들을 구한다.
# 3. 계산해준다.
# 옆 리스트로 넘어갈때 W와 B가 다른지 확인한다.
# 8개에서 4개이상이면 빼지말고 64개에서 32개이상이면 빼준다.

N, M = map(int, input().split())
lst = [list(input()) for i in range (N)]
# print (lst)

cnt = 65
n = 0
while 8+ n <= N :
    m = 0
    while 8 + m <= M :
        b = lst[n][m]
        tmp = 0
        for i in range (n, 8 + n) :
            for j in range (m, 8 + m) :
                if (n + m + i + j) % 2 == 0 :
                    if lst[i][j] != b :
                        tmp += 1
                else :
                    if lst[i][j] == b :
                        tmp += 1
        #print(tmp)
        if tmp > 32 : tmp = 64 -tmp
        if tmp < cnt : cnt = tmp
        m += 1
    n += 1
print(cnt)