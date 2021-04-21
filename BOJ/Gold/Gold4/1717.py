import sys
input = sys.stdin.readline

def find(n) : #루트 찾기
    if (p[n] < 0) : return n # 루트 반환
    p[n] = find(p[n]) # 루트찾기
    return p[n]
def merge(a, b) :
    a = find(a) # 루트
    b = find(b) # 루트
    if (a == b) : return # 루트가 같으면 종료
    p[b] = a # b집합의 루트를 a에 속하게함.

# __main__
N, M = map(int,input().split())
p = [-1] * (N+1)
for i in range (M) :
    tmp = list(map(int, input().split()))
    if tmp[0] == 0 :
        merge(tmp[1], tmp[2])
    elif tmp[0] == 1:
        if (find(tmp[1]) == find(tmp[2])) :
            print("YES")
        else : print("NO")