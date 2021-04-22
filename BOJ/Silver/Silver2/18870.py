N = int(input())
lst = list(map(int,input().split()))

lst = [[idx, val] for idx, val in enumerate (lst)]
lst.sort(key=lambda x : x[1])
#print(lst)

now = 0
newY = [0]*N 
for i in range (N) :
    if i != 0 and lst[i][1] > lst[i-1][1] : now += 1
    newY[i] = now 
#print(lst)
for i in range (N) :
    lst[i][1] = newY[i]
lst.sort()
print(*[lst[i][1] for i in range (N)])