# 뒤 두자리 자르기

# N = int(input())
# F = int(input())
N = 1981
F = 1
A = N // F
B = N % 100
print (B)
M = F * A % 100
print (M)
if B >= M : # 원래 두 뒷자리가 큰경우.
    if M >= F : # 더 줄일수 있는가?
        M -= M // F * F
        print (str(M).zfill(2))
    else : 
        print (str(M).zfill(2))
elif B < M : # 원래 두 뒷자리가 작은경우는 백의 자리가 넘어간것;
    print (str(M+F)[-2:].zfill(2))