import sys
input = sys.stdin.readline

def document() :
    N, X = map(int,input().split())
    tmp = list(map(int, input().split()))
    lst = [(value, idx) for idx, value in enumerate (tmp)]
    #print (lst)

    cnt = 0
    while (1) :
        a = 0
        for i in range (len(lst)) :
            if lst[0][0] < lst[i][0] :
                a = 1
                break
        if a == 0 :
            cnt += 1
            if (lst[0][1] == X) : return cnt
            lst.pop(0)
        else :
            lst.append(lst.pop(0))
        #print(lst)

T = int(input())
for i in range (T) :
    print(document())