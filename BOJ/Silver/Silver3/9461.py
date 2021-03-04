T = int(input())
lst = [1, 1, 1, 2, 2]
for i in range (T) :
    N = int(input())
    if N < len(lst) :
        print(lst[N-1])
    else :
        while len(lst) != N :
            lst.append(lst[len(lst)-1] + lst[len(lst)-5])
        print(lst[N-1])
