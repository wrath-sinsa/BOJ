N = int(input())
a,b =1,1
for i in range (N) :
    a, b= b, (a +b) % 15746
print(a)