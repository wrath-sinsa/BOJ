import sys
import heapq
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

def bits(idx) :
    #print(C)
    if C.count(1) == 2 :
        s = 0 
        for i in range (9):
            if C[i] == 0 :
                s += lst[i]
        if s == 100 :
            for i in range (9):
                if C[i] == 0 :
                    print(lst[i])
            exit()

    for i in range (9) :
        if C[i] == 0 and idx < i :
            C[i] = 1
            bits(i)
            C[i] = 0

# __main__
lst = list()
for i in range (9) :
    lst.append(int(input()))
lst.sort()
C = [0] * 9
bits(-1)