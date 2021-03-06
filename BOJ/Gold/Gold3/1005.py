import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def BFS(T) :
    lst = [(T, 0)] # heapq 사용을 위한 리스트
    ans = 0
    used = [0] * (N+1) # 지어 졌는가 확인.
    #pre_line, pre_time = 0, 0 # 6
    while len(lst) != 0 :
        now, line = pop(lst) # 4
        used[now] = 1
        ans += time[now-1] # 2
        # if pre_line == line : # 6 
        #     ans -= pre_time # 6
        #pre_time = time[now-1] # 6
        if now == W : return ans

        for i in build[now] : # 2
            for j in range ()
            push(lst, (i, line+1)) # 3
        
# __main__
T = int(input())
for i in range (T) :
    
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    build = [list() for i in range (N+1)] # 지으면 지을수 있는 건물 리스트
    for j in range (K) :
        tmp = list(map(int, input().split()))
        build[tmp[1]].append(tmp[0])
    W = int(input())
    print(BFS(1))


# 1. 첫번째 건물을 지음 > tmp[1]에서 무슨 건물로 시작할지 체크 해주기
# 2. 첫번째 건물을 지었을 때 
# 3. 만들수 있는 건물들을 lst에 넣음
# 4. 최소heapq를 통해 가장 작은 time이 소요되는 값을 먼저 꺼냄
# 5. 반복하며 W가 나올때 리턴
# 6. 동시 시작 하는건 따로 빼주기
# 7. 

# 지으면 지어질 수 있는 건물 리스트 (N*K)
# 지어져야 지어질 수 있는 건물 리스트 (N*K)

# 매번 for문을 돌면서 다 지어졌는지 확인. (N*K)
# for i in range (N+1) :
#   for j in build[i] : # 지어져야 지어질 수 있는 건물 리스트
#       if used[j] != 0 :break
#   else : push(i) # 다 지어져있으면 푸쉬
# >> 이거하면 바로 첫 건물을 알수있음.
