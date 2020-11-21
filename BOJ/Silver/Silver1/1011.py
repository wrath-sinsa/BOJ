# 리스트 [-1, 0, 1]의 증가와 감소 코딩
# 리스트 [7, 8, 9]처럼 있을때 최소한의 공간이동을 위한 축소 논리?

T = int(input())
for i in range(T) :
    x, y = map(int, input().split())
    cnt = 0
    distance = y - x
    lst = [-1, 0, 1]
    s = 0
    while distance != 0 :
        s += lst[2]
        # s += lst[2] * (1 + lst[2]) / 2 # lst[2]를 더했을때 돌아가는것까지
        # print ("s는 %d distance는 %d" %(s,distance))
        # print ("리스트는 ",lst)
        if s > distance : 
            if lst[0] < 1 :   # 
                cnt += 1      # 1부터 더해줘야되는데 [-1, 0, 1]과 [0, 1 , 2]는
                distance -= 1 # [2,3,4] > [1,2,3]의 경우에서 제외되므로
            else :
                if lst[1] * (1 + lst[1]) / 2 < distance : # [2,3,4] 일때 distance보다 3까지의 합(6)이 작으면 4번(6+a) 크거나 같으면 3번 반복됨
                    cnt += lst[2] # lst[0](리턴 개수) + 더해줄 값 1번
                    # print(2, cnt)
                    distance = 0
                else : 
                    cnt += lst[1]
                    # print(1, cnt)
                    distance = 0
        elif s == distance :
            cnt += lst[2]
            distance -= s
        else :
            distance -= lst[2]
            cnt += 1
            lst = [i+1 for i in lst]
    print(cnt)


# distance : algo
# 1 : 1
# 2 : 1, 1
# 3 : 1, 1, 1
# 4 : 1, 2, 1
# 5 : 1, 2, 1, 1
# 6 : 1, 2, 2, 1 
# 7 : 1, 2, 2, 1, 1
# 8 : 1, 2, 2, 2, 1 
# 9 : 1, 2, 3, 2, 1

# ...
# distance 가 얼마나 클 지 모르므로 lst값에서 최대값만 선정.
# 그러나 가장 빨리 줄였을때보다 크다면 줄이기 시작. 

# ... > 3 > 1, ... > 2 > 1 
# 1 > 2 > 3 > 4 > 5 ## n(1+n)/2 = 15 
# 1 > 3 > 5 > 7 > 9 ## n(1+(2n-1))/2 = 25
# 1 > 3 > 5 ## 9
# 5 > 3 > 2 > 1 ## 11
# 9 > 7 > 6 > 5 > 4 > 3 > 2 > 1 ## 37
# 6 > 6 > 6 > 6 > 4 > 3 > 2 > 1 >  ## 34
# 7 > 7 > 7 > 5 > 4 > 3 > 2 > 1 ## 36

### 
#생각을 잘못했음
# 줄이는거는 5 > 3 > 1, 5 > 3 > 2 > 1 도 아니고 그냥 5 > 4 > 3 > 2 > 1 임