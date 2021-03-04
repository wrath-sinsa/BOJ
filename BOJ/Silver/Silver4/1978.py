# import sys

# lst = list(range(1000))
# lst[1] = 0
# for i in range (1000) :
#     if lst[i] != 0 :
#         j = 2
#         while 1000 > i*j :
#             lst[i*j] = 0
#             j += 1
# zc = lst.count(0)
# for i in range (zc) :
#     lst.remove(0)

# N = int(sys.stdin.readline())
# cnt = 0
# for i in sys.stdin.readline().split() :
#     if int(i) in lst :
#         cnt += 1
# print(cnt)

## 2.
import sys
N = int(sys.stdin.readline())
cnt = 0
for j in map(int, sys.stdin.readline().split()) :
    if j == 1: continue
    for k in range (2, int(j**0.5) + 1) :
        if j % k == 0 :
            break
    else : 
        cnt += 1
    continue
print(cnt)
