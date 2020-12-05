for _ in range (int(input())) :
    a, b= 0, 1
    P, Q = map(int, input().split())
    for i in range (P) :
        a, b = b, a + b
    a %= Q
    print("Case #%d: %d"%(_+1, a))
    