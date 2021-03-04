N = int(input())

lst = []
for i in range (N) :
    lst.append(int(input()))
for i in sorted(lst) :
    print (i)