import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

def BFS() :
    lst = [] # heapq 사용을 위한 리스트
    ans = 0
    for i in range (1, N+1) : ## 초기화 # N
        if indegree[i] == 0 :
            push(lst, (time[i-1], i))
            dist[i] = time[i-1]
    #print(dist)

    while len(lst) != 0 :
        t, now = pop(lst) # 4

        #print (ans, lst)
        if now == W : return dist[W]# 5 답처리

        for nxt in build[now] : # N
            indegree[nxt] -= 1
            if indegree[nxt] == 0 :
                push(lst, (time[nxt-1], nxt))
            if dist[nxt] < dist[now] + time[nxt-1] : # indegree를 돌며 dist[now]가 커질때 갱신
                dist[nxt] = dist[now] + time[nxt-1] 
        #print(dist)     
                
        #print(lst)

# __main__
T = int(input())
for i in range (T) :
    
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    build = [list() for i in range (N+1)] # 지으면 지을수 있는 건물 리스트
    indegree = [0] * (N+1)
    dist = [0] * (N+1)
    for j in range (K) :
        tmp = list(map(int, input().split()))
        build[tmp[0]].append(tmp[1])
        indegree[tmp[1]] += 1
    W = int(input())
    print(BFS())


# 1. 첫번째 건물을 지음 > tmp[1]에서 무슨 건물로 시작할지 체크 해주기
# 2. 첫번째 건물을 지었을 때 
# 3. 만들수 있는 건물들을 lst에 넣음
# 4. 최소heapq를 통해 가장 작은 time이 소요되는 값을 먼저 꺼냄
# 5. 반복하며 W가 나올때 리턴
# 6. 동시 시작 하는건 따로 빼주기
# 7. 필요한 건물만 짓기!! 

# 지으면 지어질 수 있는 건물 리스트 (N*K)
# 지어져야 지어질 수 있는 건물 리스트 (N*K)

# 매번 for문을 돌면서 다 지어졌는지 확인. (N*K)
# for i in range (N+1) :
#   for j in build[i] : # 지어져야 지어질 수 있는 건물 리스트
#       if used[j] != 0 :break
#   else : push(i) # 다 지어져있으면 푸쉬
# >> 이거하면 바로 첫 건물을 알수있음.
