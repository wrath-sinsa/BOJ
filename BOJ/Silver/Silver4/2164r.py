import sys

lst = list(range(1,int(sys.stdin.readline())+1))[::-1]
if len(lst) == 1 :
    print (1)
    exit()
s = 0
for i in range(2, len(lst)+2 - 1) :
    s += 2
    if s > i :
        s = 2
print(s)

# 어떤 큐 규칙이 있는거같은데..