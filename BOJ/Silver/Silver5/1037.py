# 1과 N을 제외한 약수를 가져야하므로 소수를 제외하고 4부터 시작
N = int(input())
lst = list(map(int, input().split()))
if N == 1 :
    print(lst[0] ** 2)
else :
    print(max(lst) * min(lst))