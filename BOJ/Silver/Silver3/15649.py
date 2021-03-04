# def print_sequence(K) :
#     if K == M :
#         for i in range (M) :
#             print (lst[i], end = " ") 
#         print("")
#         return
#     for i in range (N) :
#         if used_lst[i] == False :
#             lst[K] = i + 1
#             used_lst[i] = True
#             print_sequence(K+1)
#             used_lst[i] = False

# N, M = map(int, input().split())
# lst = [0] * N
# used_lst = [False] * N
# print_sequence(0)

#re
l = input()
print (l[0], l[1], l[2])
print (type(l))