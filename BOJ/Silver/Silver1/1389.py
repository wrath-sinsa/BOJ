import sys
from queue import PriorityQueue

N, M = map(int, sys.stdin.readline().split())

nod_lst = [[] for i in range (N+1)]
for i in range (M) :
    a, b = map(int, sys.stdin.readline().split())
    nod_lst[a].append(b)
    nod_lst[b].append(a)

def BFS() :
    while len(lst) != 0 :
        now = lst.get()
        

for i in range (1, N+1) :
    lst = PriorityQueue()
    lst.put([0, 1]) # cost, idx
    used_lst = [0] * (N+1) # 리스트를 사용 했는지 

