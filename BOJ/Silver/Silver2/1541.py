import sys
from collections import deque
input = sys.stdin.readline

# __main__
s = input().rstrip()
lst = deque()
j = 0
for i in range (len(s)) :
    if s[i] == "+" :
        lst.append(s[j:i])
        lst.append("+")
        j = i+1
    elif s[i] == "-" :
        lst.append(s[j:i])
        lst.append("-")
        j = i+1
lst.append(s[j:])

#print(lst)
while len(lst) != 1 and lst[1] == "+" :
    a = lst.popleft()
    lst.popleft()
    b = lst.popleft()
    lst.appendleft(int(a) + int(b))
    #print(lst)
while (len(lst) != 1) :
    a = lst.popleft()
    lst.popleft()
    b = lst.popleft()
    lst.appendleft(int(a) - int(b))
    #print(lst)
print (lst[0])
## 77+44-52+62+62-45-65