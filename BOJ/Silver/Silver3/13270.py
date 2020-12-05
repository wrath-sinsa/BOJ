a, b = 0, 1
N = int(input())
Minimum = N // 2 if N % 2 == 0 else N // 2 -1 +2
Maximum = 0
while N != 0 :
    if N % 3 == 0 :
        Maximum += 2 * (N // 3)
        N = 0
        continue
    a, b= 1, 1
    while b <= N :
        a ,b = b, a+ b
    if a + 1 == N : # 했을때 1명이 남는경우
        N -= b - a
        Maximum += 2*a - b # a - (b - a)
    else :
        N -= a
        Maximum += b - a
print(Minimum, Maximum)

# while b <= N : 에서 (7 줄)
# 4명일때 b < n 이라면 2, 3에서 3, 5 사람수가 a가 됨.
# 3명일때 2, 3 에서는 사람수가 b가 되므로 달라짐
# 그래서 등호 넣으면
# 4명일때 3,5 사람수 a
# 3명일때 3,5 사람수 a 로 같아짐.

# 2/3이 가장 효율이 좋다,,,