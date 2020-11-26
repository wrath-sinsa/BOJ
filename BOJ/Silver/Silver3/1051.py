N, M = map(int, input().split())
lst = []
for i in range (N):
    tmp_lst = list(str(input()))
    lst.append(tmp_lst)
if N > M : 
    Minimum = M 
else :
    Minimum = N 
s = 1
while s == 1 :
    for i in range (N) :
        for j in range (M) :
            x = j + Minimum -1
            y = i
            if x >= M : # x가 리스트에 없을 경우
                continue # i가 다음걸로 넘어감
            elif lst[i][j] == lst[y][x] : # 오른쪽 꼭짓점과 비교
                move_x_lst = [0,Minimum-1]
                y += Minimum - 1
                if y >= N : # y가 리스트에 없을 경우
                    break # j포문 종료 > i 포문 종료
                for k in range (2) :
                    x = j + move_x_lst[k]
                    if lst[i][j] != lst[y][x] :
                        break # k문 종료 해서 else로 안가게함
                else : # 다 같은 경우 정사각형 인식
                    s = Minimum  ** 2
                    break # j포문 종료 > i 포문 종료
        else :
            continue
        break
         # j포문이 종료 될 경우 i포문도 끊음
    Minimum -= 1
    if Minimum == 0 :
        break
print (s)