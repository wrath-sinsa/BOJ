N, K = map(int, input().split())

lst = [[N, 0]]

used_lst = [0] * 100001
used_lst[N] = 1

def BFS() :
    while len(lst) != 0 :
        now = lst.pop(0)
        where = now[0]
        time = now[1]

        if where == K : return time

        if 2*where < 100001 and used_lst[2*where] == 0 : 
            lst.append([2*where, time + 1])
            used_lst[2*where] = 1
        if where+1 < 100001 and used_lst[where+1] == 0 : 
            lst.append([where+1, time + 1])
            used_lst[where+1] = 1
        if where-1 >= 0 and used_lst[where-1] == 0 : 
            lst.append([where-1, time + 1])
            used_lst[where-1] = 1
if N > K : print (N - K)
else : print(BFS())