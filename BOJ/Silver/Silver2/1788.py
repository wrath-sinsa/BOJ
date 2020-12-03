a, b = 0, 1
N = int(input())
for i in range (abs(N)) :
    a, b = b, (a + b) % 1000000000
if N < 0 and N % 2 == 0 :
    a *= -1
    print(-1)
elif N == 0 :
    print(0)
else :
    print(1)
print(abs(a))
