import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def conquer(u,d,l,r) :
    global CNT, ANS
    if u == R-1 :
        if l == C-1 : ANS = CNT
        CNT+=1
        if r == C-1 : ANS = CNT
        CNT+=1
    else : CNT += 2
    if d == R-1 :
        if l == C-1 : ANS = CNT
        CNT+=1
        if r == C-1 : ANS = CNT
        CNT+=1
    else : CNT += 2
def divide(u,d,l,r) : # 분할 # 1, 16, 1, 16
    print(u,d,l,r)
    # for i in range (u-1,d) :
    #     for j in range (l-1, r) :
    #         print (0, end = " ")
    #     print("")
    if d-u>1 :
        if r-l > 1:
            divide(u,d//2,l,(l+r)//2) # 1, 8, 1, 8 # 1, 4, 1 ,4 # 1, 2, 1, 2
            divide(u,d//2,(l+r)//2+1,r) # 1, 8, 9, 16 # 1, 4, 9, 16, 1, 2, 9, 16
        # else :
        #     divide(u,d//2,l,r)
        #     divide(u,d//2,l,r)
    else : conquer(u,d,l,r)


# __main__
N, R, C = list(map(int,input().split()))
global CNT, ANS
CNT = 0
ANS = 0
divide(1, 2**N, 1, 2**N)
print(ANS)