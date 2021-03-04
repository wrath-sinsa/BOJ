import sys
input = sys.stdin.readline

def add(s, x) :
    s = s|1<<x 
    return s

def remove(s, x):
    s = s&~(1<<x)
    return s

def check(s, x) :
    print(bin(s)[2:].rjust(20,"0")[-x])

def toggle(s, x):
    s = s^1<<x
    return s

def all(s) :
    s = 0b11111111111111111111
    return s

def empty(s) :
    s = 0b0
    return s

M = int(input())
S = 0b0
for i in range (M) :
    order = input().rstrip().split()
    if order[0] == "add" :
        S = add(S, int(order[1])-1)
    elif order[0] == "remove" :
        S = remove(S, int(order[1])-1)
    elif order[0] == "check" :
        check(S, int(order[1]))
    elif order[0] == "toggle" :
        S = toggle(S, int(order[1])-1)
    elif order[0] == "all" :
        S = all(S)
    elif order[0] == "empty" :
        S = empty(S)
    #print(bin(S)[2:].rjust(20,"0"))