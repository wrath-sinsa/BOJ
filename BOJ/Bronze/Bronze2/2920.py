import sys

S = list(map(int,sys.stdin.readline().split()))
for i in range (8) :
    if S[i] != i+1 :
        break
else :
    print("ascending")
    exit()
for i in range (8) :
    if S[i] != 8 - i :
        break
else :
    print("descending")
    exit()
print("mixed") 
