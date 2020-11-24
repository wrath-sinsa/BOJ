# def ispower2(N) :
#     i = 2
#     while i ** 2 <= N :
#         if N % (i ** 2) == 0 :
#             return False
#         i += 1  
#     return True

# Minimum, Maximum = map(int, input().split())
# length = Maximum - Minimum + 1
# cnt = 0
# for i in range (length) :
#     if ispower2(Minimum + i) :
#         cnt += 1 
#         print (Minimum + i)
# print (cnt)

####################

# def sqrt_sosu(N) :
#     N = (N ** 0.5)
#     lst = []
#     i = 2
#     while N >= i  : 
#         for j in range (2, (i // 2)+1) :
#             if i % j == 0 :
#                 break
#         else :
#             lst.append(i ** 2) # 소수 제곱값 넣어줌
#         i += 1
#     return lst

######################

def power2(N) :
    sosu_lst = [2,3, 5,7,11,13,17,19]
    lst = [4, 9, 25, 49, 121, 169, 289, 361]
    for i in range (20, int(N** 0.5)+1) :
        for j in range (len(sosu_lst)) :
            if i ** 2 % (sosu_lst[j] ** 2) == 0:
                break
        else :
            lst.append(i ** 2)
    return lst



def isnotpower2(Minimum, Maximum) :
    sq_sqrt_lst = power2(Maximum)
    # print(sq_sqrt_lst)
    lst = list(range(Minimum, Maximum+1))
    # cnt = 0
    for i in range (len(sq_sqrt_lst)) :
        j = Minimum // sq_sqrt_lst[i] # 4, 9, 25, 49로 나눴을때 몫
        # print("그대로", j)
        if Minimum / sq_sqrt_lst[i] != j : # 위 몫의 소수점이 버려진경우
            j += 1
            # print("+1한거", j)
        while Maximum >= sq_sqrt_lst[i] * j :
            try :
                # cnt += 1
                # print(cnt)
                # print (sq_sqrt_lst[i] * j, lst.index(sq_sqrt_lst[i] * j))
                # lst[lst.index(sq_sqrt_lst[i] * j)] = 0
                lst.remove(lst[lst.index(sq_sqrt_lst[i] * j)])
            except ValueError :
                pass
            j += 1
    # while lst.count(0) != 0 :
    #     print(lst.count(0))
    #     lst.remove(0)
    return len(lst)

Minimum, Maximum = map(int, input().split())
print(isnotpower2(Minimum, Maximum))

# def power2(N) :
#     sosu_lst = [2,3, 5,7,11,13,17,19]
#     lst = [4, 9, 25, 49, 121, 169, 289, 361]
#     for i in range (20, int(N** 0.5)+1) :
#         for j in range (len(sosu_lst)) :
#             if i ** 2 % (sosu_lst[j] ** 2) == 0:
#                 break
#         else :
#             lst.append(i ** 2)
#     return lst



# def isnotpower2(Minimum, Maximum) :
#     sq_sqrt_lst = power2(Maximum)
#     lst = list(range(Minimum, Maximum+1))
#     for i in range (len(sq_sqrt_lst)) :
#         j = Minimum // sq_sqrt_lst[i]
#         if Minimum / sq_sqrt_lst[i] != j :
#             j += 1
#         while Maximum >= sq_sqrt_lst[i] * j :
#             if sq_sqrt_lst[i] * j >= Minimum:
#                 try :
#                     lst[lst.index(sq_sqrt_lst[i] * j)] = 0
#                 except ValueError :
#                     pass
#             j += 1
#     lst = [lst[i] for i in range (len(lst)) if lst[i] != 0]
#     return len(lst)

# Minimum, Maximum = map(int, input().split())
# print(isnotpower2(Minimum, Maximum))