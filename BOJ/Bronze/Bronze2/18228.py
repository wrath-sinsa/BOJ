N = int(input())
lst = list(map(int,input().split()))
fnd = lst.index(-1)
lst1 = lst[:fnd]
lst2 = lst[fnd+1:]
print(min(lst1) + min(lst2))