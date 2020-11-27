N, K = map(int, input().split())
cnt = 0

# 시간 복잡도는 O(log n)으로 예상됨>> N // 2
def lst_make (lst, N, exponent) : # lst 리턴 하고싶음
    if N < 2 :
        lst.append(2 ** exponent)
        return lst
    elif N % 2 == 0 :
        return lst_make(lst, N // 2, exponent + 1)
    else :
        lst.append(2 ** exponent)
        return lst_make(lst, N // 2, exponent + 1)

## 요 부분을 재귀 함수로 만들어볼까함
# if N > 2 :
#     if N % 2 == 0 : 
#         lst = [2] * (N // 2)
#     else :
#         lst = [2] * (N // 2)
#         lst.append(1)
#     print(lst)

lst = lst_make ([], N, 0)
print(lst, sum(lst))
while len(lst) > K :  
    cnt += lst[0]
    print(cnt)
    lst.insert(0, lst.pop(0)*2)
    while len(lst) > 1 and lst[0] == lst[1] :
        tmp = lst.pop(0)
        lst.pop(0)
        lst.insert(0, tmp*2)
    print(lst)
print(cnt)