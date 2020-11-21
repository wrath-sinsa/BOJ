# 이것도 재귀로 풀어보기 
# W인 것을 잡아서 거꾸로 진행
# 이미 만들어진 경우 제외....

def calculate(limit) :
    global time_cnt
    tmp_W = limit[0]

    if tmp_W not in build_lst :
        time_cnt += build_cast[tmp_W - 1]
        build_lst.append(tmp_W)
    
    if tmp_W == 1 : return

    for tmp_limit in build_limit :
        if tmp_limit[1] == tmp_W :
            calculate(tmp_limit)

    
        
T = int(input())
for i in range (T) :
    N, K = map(int, input().split()) # 건물 개수, 건설 규칙

    build_cast = list(map(int, input().split()))

    build_limit = [list(map(int, input().split())) for j in range (K)]
    build_limit.sort(key = lambda x : x[1], reverse=True)

    W = int(input()) # 지어야 할 건물 번호

    global time_cnt
    time_cnt = build_cast[W-1]
    build_lst = [W] # W 지어졌다
    for limit in build_limit :
        if limit[1] == W :
            calculate(limit)
    print (time_cnt)

# 7 > 6
# 7 > 5 

# build_cast = []
# for j in range (N) :
#     D = int(input()) # 건물 짓는 시간
#     build_cast.append(D)

# for j in range (K) :
#     X, Y = map(int, input().split()) # X를 지어야 Y를 지을 수 있다.
#     build_limit.append([X, Y])