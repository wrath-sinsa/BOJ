N = int(input())
cnt = 0
while N % 5 != 0 :
    N -= 3
    if N < 0 :
        print(-1)
        exit()
    cnt += 1
if N % 5 != 0 : 
    print(-1)
    exit()
cnt += N // 5
print(cnt)