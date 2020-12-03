X, Y = map(int, input().split())
Z_int = Y * 100 //X
Z_double = Y * 100 / X
print(Z_int, Z_double)
cnt = 0
if Z_int > 98 :
    print (-1)
    exit()
while Z_int == Y * 100 //X :
    Y += 1
    X += 1
    print(Y * 100/X)
    cnt += 1
print(cnt)
