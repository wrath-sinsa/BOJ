N = str(input())
tmp_N = int(N)
f = lambda x : int(x[0]) + int(x[1])
cnt = 0
while 1:
    if tmp_N < 10 :
        tmp_N *= 2
        continue
    f(str(tmp_N))
    cnt += 1
    if tmp_N == N : break