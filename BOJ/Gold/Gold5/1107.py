import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
M = int(input())
if (M) :
    broken = input().split()
    ans = abs(N-100)
    for i in range (0, 5000000) : # 이동
        str_i = str(i)
        for j in str_i:
            if j in broken : break
        else : 
            #print(i)
            tmp = abs(N-i)
            tmp += len(str_i)
            if tmp < ans : 
                ans = tmp
    print (ans)
else : 
    if N == 100 : print(0)
    else : print(min(abs(N-100), len(str(N))))