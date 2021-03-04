X = int(input())
ans_lst = [0] * (X+1)
def cal(x) :
    tmp3 = 0
    tmp2 = 0
    print(x)
    if x == 1 : return 1
    if ans_lst[x] == 0 :
        if x % 3 == 0 : tmp3 = cal(x//3)
        if x % 2 == 0 :
            tmp2 = cal(x//2) 
            if tmp3 != 0 :
                if tmp2 > tmp3 : tmp2, tmp3 = tmp3, tmp2
        tmp1 = cal(x-1)
        if tmp2 != 0 :
            if tmp2 < tmp1 : tmp1, tmp2 = tmp2, tmp1
        if tmp3 != 0 :
            if tmp3 < tmp1 : tmp1, tmp3 = tmp3, tmp1
        ans_lst[x] = tmp1  
        print(tmp1, tmp2, tmp3)
    return ans_lst[x]

print(cal(X))