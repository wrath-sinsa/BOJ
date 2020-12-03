N, A, B = map(int, input().split())
d = abs(A - B)
day = 1
while d != 0 : # 완료 조건
    if A < 1 or B < 1 or A > N or B > N : # 제한 조건
        break
    
    move = 2 ** (day - 1)


else :
    print(day)
print(-1)