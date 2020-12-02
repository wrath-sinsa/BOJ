X = int(input())
lst = [1, 2, 4, 8, 16, 32, 64]
cnt = 0
while X != 0 :
    for i in range (len(lst)) :
        if lst[i] > X :
            X -= lst[i-1]
            cnt += 1
            break
        elif lst[i] == X:
            X -= lst[i]
            cnt += 1
            break
print (cnt)