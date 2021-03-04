import sys

# T = int(sys.stdin.readline())
# for i in range (T) :
#     S = sys.stdin.readline()
#     score = 0

#     j = 0
#     k = 1
#     while j < len(S) :
#         if S[j] == "O" :
#             score += k
#             k += 1
#         else :
#             k = 1
#         j += 1
#     print(score)

#
A = sys.stdin.readline()[:-1].split("X")
print(A)
print(sum([len(j)*(len(j)+1)//2 for j in A]))