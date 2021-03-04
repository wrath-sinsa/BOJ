# 두 숫자를 리스트로 [8,8,0,8] [8,8,8,0]

def available(a, b) :
    if a < b : return list(range(a, b+1)) # 3 5
    elif a > b : return list(range(b, 9+1)) + list(range(0, a+1)) # 9 7
    ## 둘 숫자가 같을 때 ex 8 8
def number8(k):
    if k == Rlen :
        ans = int("".join(ans_lst))
        if int(L) <= ans <= int(R) :
            return(ans)
        else : return
    lst = available(L_lst[k], R_lst[k])
    for i in range (len(lst)) :
        ans_lst.insert(k, lst[i])
        number8(k+1)


L, R = map(str, input().split())
L_lst = list(map(int,L))
R_lst = list(map(int,R))
ans_lst = []
print(L, R, L_lst, R_lst)
Rlen = len(R_lst)
while Rlen != len(L_lst) :
    L_lst.insert(0, 0)
for i in range (Rlen, 0) :
    if R_lst[i] < L_lst :
        break
number8(0)