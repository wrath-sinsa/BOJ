N = int(input()) # max = 300
lst = [int(input()) for i in range (N)]
lst.insert(0, 0)
S = 0
global ans
ans = 0
cost_lst = [[0] * (N+1) for i in range (2)]
def stair(s, n, k) :
    global ans
    print(s, n, k)
    print(cost_lst)
    ## 종료 처리
    if n > N : return # 마지막 계단을 안밟을 경우
    
    ## 실행
    # print(n)
    s += lst[n]

    ## 메모이제이션으로 확인
    if cost_lst[n] == 0 : cost_lst[n] = s
    else :
        if cost_lst[n] >= s : return
        else : cost_lst[n] = s

    # 마무리
    if n == N :
        # print (s) 
        if s > ans : # 마지막 계단을 밟았을때
            ans = s
            return

    ## 진행
    if k == 2 : # 계단을 세번 갔을때 방지
        stair(s, n+2, 1) 
        return

    stair(s, n+1, k+1) # 한 칸 오를 때
    stair(s, n+2, 1) # 두 칸 오를 때

stair(S, 0, 0)
print(ans)