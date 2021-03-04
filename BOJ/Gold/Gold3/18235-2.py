import sys

N, A, B = map(int, sys.stdin.readline().split())
if A > B : A, B= B, A
dis_bin = bin(abs(B - A))[2:][::-1]
length = len(dis_bin) - 1
# 완료 조건
def cal(A, B, i) :  
    if A == B : return True # if i > length return True
    i += 1
    move = 2 ** (i -1)

    if i == 0 :
        if dis_bin[i] == "1" : return False
        else : 
            if (cal(A, B, i)) : return True
            else : return False

    if dis_bin[i] == "1" :
        if (cal(A +move, B - move, i)) : return True
    elif dis_bin[i] == "0" :
        if (A - move > 0) :
            if (cal(A-move, B-move, i)) : return True
        if (B + move <= N) :
            if (cal(A+move, B+move, i)) : return True
    return False

# 실행
if(cal(A,B,-1)): print(length)
else : print (-1)