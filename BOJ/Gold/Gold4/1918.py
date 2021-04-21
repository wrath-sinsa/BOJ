import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

#N = int(input())
#N, M = map(int,input().split())

def a(n) :
    if n == "(" or n == ")" : return 0
    elif n == "+" or n == "-" : return 1
    elif n == "*" or n == "/" : return 2

S = input().rstrip()
lst = list()
for i in range (len(S)) :
    #print(ord(S[i]))
    if 0 <= ord(S[i]) -65 < 26 :
        print(S[i], end= "")
    elif S[i] == "(" :
        lst.append("(")
    elif S[i] == ")" :
        #print(lst)
        while lst[-1] != "(" :
            print(lst.pop(), end ="")
        lst.pop()
    else:
        while lst :
            if a(S[i]) <= a(lst[-1]) :
                print(lst.pop(), end = "")
            else : break
        lst.append(S[i])
while lst :
    print(lst.pop(), end= "")

# AB+CDE**FGHF*++++