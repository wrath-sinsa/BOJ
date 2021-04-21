import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop

################################################ 역으로 돌기! 실패!
def BFS() :
    lst = [] # heapq 사용을 위한 리스트
    ans = 0
    used = [0] * (N+1) # 지어 졌는가 확인.
    push(lst, [time[W-1], W])

    while len(lst) != 0 : # N개를 돌아야함.
        t, now = pop(lst) # 4
        print (t, now,)
        used[now] = 1 # 건물 짓기

        print (used)
        ans += t # 2 # 동시에 지어지는 라인일 경우 빼기
        for i in range (len(lst)) : # 6 # N
            lst[i][0] -= t # 6

        for nxt in build[now] : # N
            for j in build_b[nxt] : 
                print (j, lst)
                if used[j] == 0 : break ##### 얘 때매 버려지면 다시 고르기가;;
            else : 
                push(lst, [time[nxt-1], nxt])
            

        #print(lst)
    return ans

# __main__
T = int(input())
for i in range (T) :
    
    N, K = map(int, input().split())
    time = list(map(int, input().split()))
    build = [list() for i in range (N+1)] # 지으면 지을수 있는 건물 리스트
    build_b = [list() for i in range (N+1)]
    for j in range (K) :
        tmp = list(map(int, input().split()))
        build[tmp[1]].append(tmp[0])
        build_b[tmp[0]].append(tmp[1])
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
