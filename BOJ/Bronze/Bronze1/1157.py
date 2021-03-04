A = input()
A = A.upper()
B = set(A)
cnt_lst = [0]
C = 0
for i in B :
    tmp_cnt = 0
    where = A.find(i)
    while where != -1 :
        where = A.find(i, where+1)
        tmp_cnt += 1
    if tmp_cnt > cnt_lst[0] :
        cnt_lst = [tmp_cnt]
        C = i
    elif tmp_cnt == cnt_lst[0] :
        cnt_lst.append(0)
if len(cnt_lst) > 1:
    print("?")
else :
    print(C)
