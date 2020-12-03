
# def fibonacci (N) :
#     lst0 = [1,0,1,1]
#     lst1 = [0,1,1,2]
#     n = 0
#     if 0 <= N < 4 :
#         print ("%d %d" %(lst0[N], lst1[N]))
#         return 0
#     while len(lst0) != N +1 :
#         lst0.append(lst0[2+n] + lst0[3+n])
#         lst1.append(lst1[2+n] + lst1[3+n])
#         n += 1
#     print ("%d %d" %(lst0.pop(), lst1.pop()))

# T = int(input())

# for i in range (T):
#     N = int(input())
#     fibonacci(N)

# re
# exec("a,b=1,0;exec('a,b=b,a+b;'*int(input()));print(a,b);"*int(input()))
# # 뭔지도 모르겠다...
# exec(int(input())*'p,q=1,0;exec("p,q=q,p+q;"*int(input()));print(p,q);')

# re
for _ in range(int(input())):
    A,B=1,0
    for i in range(int(input())):A,B=B,A+B
    print(A,B)