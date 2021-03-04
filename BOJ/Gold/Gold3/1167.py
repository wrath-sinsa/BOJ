import sys
input = sys.stdin.readline

V = int(input())

tree = [list() for i in range (V+1)]
for i in range (V) :
    tmp = list(map(int, input().split()))
    for i in range ((len(tmp) - 2)//2) :
        tree[tmp[0]].append((tmp[2*i+1], tmp[2*i+2])) 
print(tree)
