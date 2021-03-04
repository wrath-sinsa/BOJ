import sys

N, A, B = map(int, sys.stdin.readline().split())
dis_bin = bin(abs(B - A))[2:][::-1]
length = len(dis_bin) - 1
#print(dis_bin, A, B)
# 완료 조건
def cal(A, B, i) :  
    if A == B : return True # if i > length return True
    i += 1
    if i == 0 :
        if dis_bin[i] == "1" :
            return False
        else :
            if(cal(A, B, i)) : return True
            else : return False
    if dis_bin[i] == "1" :
        if(move1(A, B, i) == False) :
            return False
    elif dis_bin[i] == "0" :
        if(move2(A, B, i) == False) :
            return False
    return True
def move1(A, B, i) :
    if A > B : A, B = B, A
    A += 2 ** (i - 1) # 우
    B -= 2 ** (i - 1) # 좌
    return cal(A, B, i)

def move2(A, B, i) :
    if A > B : A, B = B, A
    x1 = A - 2 ** (i - 1) # 좌
    x2 = B - 2 ** (i - 1) # 좌
    if 0 < x1 :
        a = x1
        b = x2
        if(cal(a,b,i)) : return True
    x1 = A + 2 ** (i - 1) # 우
    x2 = B + 2 ** (i - 1) # 우
    if x2 <= N :
        a = x1
        b = x2
        if(cal(a,b,i)) : return True
    return False

# 실행
if(cal(A,B,-1)): print(length)
else : print (-1)