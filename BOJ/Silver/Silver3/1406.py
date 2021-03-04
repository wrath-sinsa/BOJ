import sys
input = sys.stdin.readline
lst = list(input())[:-1]
N = len(lst)
M = int(input())
cursor = N
for i in range (M) :
    order = input()[:-1]
    if order =="L" :
        if cursor > 0 : cursor -= 1
    elif order == "D" :
        if cursor < N : cursor += 1
    elif order == "B" :
        if cursor != 0 :
            lst.pop(cursor-1)
            cursor -= 1
            N -= 1
    else :
        lst.insert(cursor, order[2])
        cursor += 1
        N += 1
print("".join(lst))