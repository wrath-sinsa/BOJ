N, M = map(int, input().split())
brand_lst = []
for i in range (M):
    tmp_lst = list(map(int,input().split()))
    brand_lst.append(tmp_lst)
Min_6 = min(brand_lst, key = lambda x: x[0])[0]
Min_1 = min(brand_lst, key = lambda x: x[1])[1]
if Min_6 == 0 or Min_1 == 0 :
    print(0)
else :
    if Min_6 / 6 > Min_1 :
        print(Min_1 * N)
    elif (N % 6) * Min_1 > Min_6:
        print( ( (N // 6) + 1 ) * Min_6 )
    else :
        print((N // 6) * Min_6 + (N % 6) * Min_1)

### 한 브랜드에서 살때
# N, M = map(int, input().split())
# brand_lst = []
# for i in range(M) :
#     tmp_lst = list(map(int, input().split()))
#     brand_lst.append(tmp_lst)
# s = 100001
# for i in range (M) :
#     if brand_lst[i][0] /6 > brand_lst[i][1] :
#         a = brand_lst[i][1] * N
#     else :
#         a = ( N // 6 ) * brand_lst[i][0] + ( N % 6 ) * brand_lst[i][1]

#     if s > a :
#         s = a
# print (a)
