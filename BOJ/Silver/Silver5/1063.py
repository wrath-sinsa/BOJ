init_lst = list(input().split())
#굳이 초기화
init_lst[0] = list(str(init_lst[0]))
init_lst[1] = list(str(init_lst[1]))
init_lst[0][0] = ord(init_lst[0][0]) - 64
init_lst[1][0] = ord(init_lst[1][0]) - 64
init_lst[0][1] = int(init_lst[0][1])
init_lst[1][1] = int(init_lst[1][1])
init_lst[2] = int(init_lst[2])


move1_lst = ["R","L","B","T","RT","LT","RB","LB"]
move_x_lst = [1, -1, 0, 0, 1, -1, 1, -1]
move_y_lst = [0, 0, -1, 1, 1, 1, -1, -1]
for i in range (init_lst[2]) :
    move = str(input())
    x1 = init_lst[0][0] + move_x_lst[move1_lst.index(move)]
    y1 = init_lst[0][1] + move_y_lst[move1_lst.index(move)]
    if x1 < 1 or x1 > 8 or y1 < 1 or y1 > 8 :
        continue
    # 돌처리
    if x1 == init_lst[1][0] and y1 == init_lst[1][1] :
        x2 = init_lst[1][0] + move_x_lst[move1_lst.index(move)]
        y2 = init_lst[1][1] + move_y_lst[move1_lst.index(move)]
        if x2 < 1 or x2 > 8 or y2 < 1 or y2 > 8 :
            continue
        init_lst[1] = [x2, y2]
    init_lst[0] = [x1, y1]

init_lst[0][0] = chr(init_lst[0][0] + 64)
init_lst[1][0] = chr(init_lst[1][0] + 64)
init_lst[0][1] = str(init_lst[0][1])
init_lst[1][1] = str(init_lst[1][1])
init_lst[0] = "".join(init_lst[0])
init_lst[1] = "".join(init_lst[1])

print(init_lst[0])
print(init_lst[1])


## re 개쩐다....
a,b,c=input().split()
C = lambda o : [ord(o[0])-65,int(o[1])-1] # 위치 처리 / 내가한 init...
# 대신 얘는 0, 0 부터 처리를 함 // 0 ~ 7

F = lambda o : print(f'{chr(o[0]+65)}{o[1]+1}') # 프린트하는 식인데 f``는 첨봄
G = lambda o : [o[0]-1*('L'in s)+('R'in s),o[1]-1*('B'in s)+('T'in s)]
# 위 G는 좌우 상하를 판정하고 각각 값해주는 식
a,b=C(a),C(b)
for i in range(int(c)):
    s=input()
    x,y=G(a)
    if 0<=x<8 and 0<=y<8:
        if[x,y]==b:
            v,w=G(b)
            if 0<=v<8 and 0<=w<8:a,b=[x,y],[v,w]
        else:a=[x,y]
F(a);F(b)