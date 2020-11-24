N, M = map(int, input().split())
brand_lst = []
for i in range (M):
    tmp_lst = list(map(int,input().split()))
    brand_lst.append(tmp_lst)
print(tmp_lst)
Min_6 = min(tmp_lst, key = lambda x: x[0])
Min_1 = min(tmp_lst, key = lambda x: x[1])
print((N // 6) * Min_6 + (N % 6) * Min_1)
# Min_6 = brand_lst[0][0]
# for i in range (1, len(brand_lst)) :
#     if Min_6 > brand_lst[i][0] :
#         Min_6 = brand_lst[i][0]
# Min_1 = brand_lst[0][1]
# for i in range (1, len(brand_lst)) :
#     if Min_6 > brand_lst[i][1] :
#         Min_6 = brand_lst[i][1]