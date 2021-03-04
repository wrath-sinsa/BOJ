# import sys

# N = int(sys.stdin.readline())
# lst = []
# for i in range (N) :
#     string = sys.stdin.readline()[:-1]
#     if string not in lst :
#         lst.append(string)
# length = len(lst)
# for i in range (length-1) :
#     for j in range (length-1-i) :
#         if len(lst[j]) > len(lst[j+1]) :
#             lst[j], lst[j+1] = lst[j+1], lst[j]
#         if len(lst[j]) == len(lst[j+1]) and lst[j] > lst[j+1] :
#             lst[j], lst[j+1] = lst[j+1], lst[j]
# for i in lst :
#     print(i)

## re 
#ㅋㅋ 난바보야...
import sys

N = int(sys.stdin.readline())
lst = []
for i in range (N) :
    string = sys.stdin.readline()[:-1]
lst = sorted(sorted(set(lst)), key=len)
print(lst)