# lst에 넣어줄때 가장 적게 하는 곳부터 넣어주던가,
# lst에 넣고 양을 분배 하던가.

N = int(input())
limit_lst = list(map(int, input().split()))
limit_lst.sort()
M = int(input())
freight_lst = list(map(int, input().split()))
freight_lst.sort(reverse=True)
print(limit_lst, freight_lst)
if limit_lst[-1] < freight_lst[0] : # 크레인이 옮길 수 없는 경우
    print(-1)
else :
    lst = []
    for i in range (N) :
        tmp_lst = []
        while len(freight_lst) != 0 and limit_lst[i] >= freight_lst[-1] : # 오류 제한 and 범위 제한
            tmp_lst.append(freight_lst.pop(-1))
        lst.append(tmp_lst)
    print (lst)
    lst = [len(value) for value in lst]
    print (lst)
    while lst[-1] != max(lst) :
        for i in range (N-1) :
            if lst[i] > lst[i+1] :
                lst[i+1] += 1
                lst[i] -= 1
    print (lst, lst[-1])
