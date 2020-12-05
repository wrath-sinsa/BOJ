for _ in range (int(input())) :
    a, b= 0, 1
    Fn = int(input())
    if Fn == 1 :
        print (2)
        continue
    cnt = 0
    while Fn != a :
        a, b = b, a + b
        cnt += 1
    print(cnt)

    
#re
# print(2 if c==1 else c)