# 1. 원이 접할경우 1개
# 2. 원이 만나지 않을경우 0개
# 3. 원이 접하지 않고 만날경우 2개
# 4. 있는 위치가 같고 반지름까지 같은경우
# 5. 큰원 안에 작은 원이 있는경우
# 5-1 . 접하는 경우
# 5-2 . 두점에서 만나는 경우
# 5-3 . 만나지 않는경우

T = int(input())
for i in range (T) :
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    d = ( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) ) ** 0.5
    print (d)
    if x1 == x2 and y1 == y2 : # 한점에 두원
        if r1 > r2 or r1 < r2:
            print (0)
        else : # r1 == r2
            print (-1)
    elif d < r2 or d < r1 : # 큰원 안에 작은원 중심
        if r1 <= r2 :
            if d + r1 > r2 :
                print (2)
            elif d + r1 == r2: # 내접
                print (1)
            elif d + r1 < r2 :
                print (0)
        elif r2 <= r1 :
            if d + r2 > r1 :
                print (2)
            elif d + r2 == r1: # 내접
                print (1)
            elif d + r2 < r1 :
                print (0)
    else : # d >= r1 and d >= r2 # 원 바깥쪽에 다른 원
        if r1 + r2 > d : 
            print(2)
        elif r1 + r2 == d : # 외접
            print(1)
        elif r1 + r2 < d :
            print(0)

# x1, y1, r1, x2, y2, r2 = 1, 1, 1, 1, 1, 5
# d = ( ((x2 - x1) ** 2) + ((y2 - y1) ** 2) ) ** 0.5
# print (d, r1 ,r2)
# if x1 == x2 and y1 == y2 :
#     if r1 > r2 or r1 < r2:
#         print (0)
#     else :
#         print (-1)
#     # continue
# elif r1 < d < r2 or r2 < d < r1 : # 큰원 안에 작은원 중심
#     if r1 < d :
#         if d + r1 > r2 :
#             print (2)
#         elif d + r1 == r2:
#             print (1)
#         elif d + r1 < r2 :
#             print (0)
#     elif r2 < d :
#         if d + r2 > r1 :
#             print (2)
#         elif d + r2 == r1:
#             print (1)
#         elif d + r2 < r1 :
#             print (0)
# else :   
#     if r1 + r2 > d :
#         print(2)
#     elif r1 + r2 == d :
#         print(1)
#     elif r1 + r2 < d :
#         print(0)