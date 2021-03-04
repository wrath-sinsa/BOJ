N = int(input())
lst = [list(map(int, input().split())) for i in range (N)]
ans_lst = []
a = len(ans_lst)
while a != N :
    ans_lst.append([min(lst[a]),lst.index(min(lst[a])) ])
        

    a += 1