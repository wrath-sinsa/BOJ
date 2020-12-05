for _ in range (int(input())):
    N = int(input())
    lst = []
    while N != 0 :
        a, b = 0, 1
        while b <= N :
            a, b = b, a + b
        lst.append(a)
        N -= a
    for i in reversed(lst) :
        print(i, end=" ")