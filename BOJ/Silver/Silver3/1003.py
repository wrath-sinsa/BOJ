
def fibonacci (N) :
    lst0 = [1,0,1,1]
    lst1 = [0,1,1,2]
    n = 0
    if 0 <= N < 4 :
        print ("%d %d" %(lst0[N], lst1[N]))
        return 0
    while len(lst0) != N +1 :
        lst0.append(lst0[2+n] + lst0[3+n])
        lst1.append(lst1[2+n] + lst1[3+n])
        n += 1
    print ("%d %d" %(lst0.pop(), lst1.pop()))

T = int(input())

for i in range (T):
    N = int(input())
    fibonacci(N)
