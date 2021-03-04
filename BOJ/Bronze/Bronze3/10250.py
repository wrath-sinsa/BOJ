T = int(input())
for i in range (T) :
    H, W, N = map(int, input().split())
    I_W = (N // H) + 1 # N = 10 H = 6 일때 2
    I_H = N % H # N = 10 H = 6 일때 4
    if I_H == 0 :
        I_H = H
        I_W -= 1
    print("".join(str(I_H)+str(I_W).zfill(2)))