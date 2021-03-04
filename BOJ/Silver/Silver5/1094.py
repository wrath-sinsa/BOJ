# X = int(input())
# lst = [1, 2, 4, 8, 16, 32, 64]
# cnt = 0
# while X != 0 :
#     for i in range (len(lst)) :
#         if lst[i] > X :
#             X -= lst[i-1]
#             cnt += 1
#             break
#         elif lst[i] == X:
#             X -= lst[i]
#             cnt += 1
#             break
# print (cnt)

N = int(input())
s = ""
while N != 0:
    if N % 2 == 1 :s += "1"
    else : s += "0"
    N//=2
print(s.count("1"))