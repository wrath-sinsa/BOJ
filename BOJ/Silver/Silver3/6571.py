while 1:
    A, B = map(int, input().split())
    if A == 0 and B == 0 :
        break
    a, b = 1, 2
    cnt = 0
    while a <= B :
        if A <= a :
            cnt += 1
        a, b = b, a + b
    print(cnt)