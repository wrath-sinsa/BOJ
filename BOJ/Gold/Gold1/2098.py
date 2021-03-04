import sys
from collections import deque
input = sys.stdin.readline

# a는 몇번째 도시로 들어왔는가, b는 bitmask 값 
def Dynamic(a, b) :
    if DP[a][b] != sys.maxsize :
        return DP[a][b]
    #print(a)
    #d.append(a) 
    if b == 2**N-1 :
        # while d :
        #     print(d.popleft()+1, end = " ")
        # print("")
        if Way[a][0] != 0:
            return Way[a][0]
        else :
            return sys.maxsize
    # 비트마스킹에서 판단해서 들어가기...
    for i in range (N) :
        if b & (1 << i) == 0 and Way[a][i] != 0 :
            nxt = b | (1 << i)
            
            x = Dynamic(i, nxt)+Way[a][i]
            # print (DP[a][b], x)

            DP[a][b] = min(DP[a][b], x)
    # # 확인용 if
    # if bin(b).count("1") == 2 :
    #    print(a, bin(b)[2:], b, DP[a][b])
    return DP[a][b]

# __main__
N = int(input())

#입력
Way = [list(map(int,input().split())) for i in range (N)]
#print(Way)

# DP
DP = [[sys.maxsize]*(int(2**N)) for i in range (N)]

# 풀이
print(Dynamic(0, 1))

#-1 비트마스킹으로 어디갔나 표시
# DP를 실행하는 과정에서 모든 루트를 들러봐야 하므로
# 비트마스킹 값을 전해주고 전부 사용하면 값저장 / 아님
# (0001) -> (0101) -> (0111) -> (1111) - > DP(0011).. / 뭐야이건
#-2 DP로 만약 n번째루트에서 사용된 최저값 표시
## 겹치는 경로라면 가는 과정이 달라지니 DP할때
## 비트마스킹의 값도 저장해야됨.
## (0101)(2) , (0110)(2) 의 경우를 생각하면됨.