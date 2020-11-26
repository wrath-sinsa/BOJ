N, A, B = map(int, input().split())
lst_A = sorted(list(map(int, input().split())), reverse=True) # 큰 순서 정렬
lst_B = sorted(list(map(int, input().split())), reverse=True) # 큰 순서 정렬
# print(lst_A, lst_B)
s = 0
if N % 2 == 1 :
    s += lst_A.pop(0)
    N -= 1
while N != 0 :
    if len(lst_A) > 1 and len(lst_B) != 0 :
        if lst_A[0] + lst_A[1] > lst_B[0] :
            s += lst_A.pop(0) + lst_A.pop(0)
            # print(lst_A, lst_B)
        else :
            s += lst_B.pop(0)
            # print(lst_A, lst_B)
        N -= 2
    elif len(lst_A) < 2 :
        while N > 1 :
            s += lst_B.pop(0)
            # print(lst_B)
            N -= 2
    elif len(lst_B) == 0 :
        while N != 0 :
            s += lst_A.pop(0)
            # print(lst_A)
            N -= 1
    # print(N)
print (s)