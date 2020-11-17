T = int(input())
lst0 = [ 1, 5, 6 ]
lst28 = [ 6, 2, 4 ,8]
lst37 = [1, 3, 9, 7]
for i in range (T) :
    A, B = map(int, input().split())
    A = A % 10
    if A in lst0 :
        print (A)
    elif A == 4 :
        if B % 2 == 1 :
            print(4)
        else :
            print(6)
    elif A == 9 :
        if B % 2 == 1 :
            print(9)
        else :
            print(1)
    elif A == 2 :
        print(lst28[(B%4) ])
    elif A == 8 :
        print (lst28[::-1][B%4-1])
    elif A == 3 :
        print (lst37[B%4])
    elif A == 7 :
        print (lst37[::-1][B%4-1])
    else :
        print(10)


if A in lst0 :
    print (A)
elif A == 4 :
    if B % 2 == 1 :
        print(4)
    else :
        print(6)
elif A == 9 :
    if B % 2 == 1 :
        print(9)
    else :
        print(1)
elif A == 2 :
    print(lst28[(B%4) ])
elif A == 8 :
    print (lst28[::-1][B%4-1])
elif A == 3 :
    print (lst37[B%4])
elif A == 7 :
    print (lst37[::-1][B%4-1])
else :
    print(10)


