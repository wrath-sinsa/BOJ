## 논리를 모르겠다...

N = int(input())
A = list(map(int, input().split()))
B = [[idx , value] for idx, value in enumerate (A)]
B.sort(key = lambda x: x[1])
for i in range (len(B)) :
    B[i].append(i)
B.sort()
for i in range (len(B)) :
    print(B[i][2], end = " ")