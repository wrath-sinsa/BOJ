import sys
input = sys.stdin.readline

def conquer(u, d, l, r) :
    global CNT, ANS
    if u == R+1 :
        if l == C+1 : ANS = CNT
        CNT += 1
        if r == C+1: ANS = CNT
        CNT += 1
    else : CNT += 2
    if d == R+1:
        if l == C+1 : ANS = CNT
        CNT += 1
        if r == C+1 : ANS = CNT    
        CNT += 1
    else : CNT += 2
def divide(u, d, l, r) : # 분할
    global CNT
    #print (u,d,l,r)
    if (u-1 <= R < d and l-1 <= C < r) == 0 : 
        CNT += (d-u+1) ** 2
        return
    if u < d - 1 : 
        divide (u, (u+d)//2, l, (l+r)//2)
        divide (u, (u+d)//2, (l+r)//2+1, r)
        divide ((u+d)//2+1, d, l, (l+r)//2)
        divide ((u+d)//2+1, d, (l+r)//2+1, r)
    else : conquer (u,d,l,r)

# __main__
N, R, C = list(map(int,input().split()))
global CNT, ANS
ANS = 0
CNT = 0
divide(1, 2**N, 1, 2**N)
print (ANS)