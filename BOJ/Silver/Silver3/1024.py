# a의 정수부분, a의 소수점 부분이 있는가 비교
# 식은 L(2a+L-1)/2 = N 이용 d = 1 , n = L 인 등차수열의 합
N, L = map(int, input().split())

a = ((N * 2 / L) + 1 - L ) // 2
lst = [int(a) + i for i in range (L)]
if a < 0 :
    lst = [-1]
else :
    while sum(lst) != N :
        L += 1
        if L > 100 or a < 1:
            lst = [-1]
            break
        a = ((N * 2 / L) + 1 - L ) // 2
        lst = [int(a) + i for i in range (L)]
for i in range (len(lst)) :
    print(lst[i], end = " ") 
