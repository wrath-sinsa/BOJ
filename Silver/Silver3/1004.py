# 점을 포함하는 원이 몇개인지 세면 될듯.
# 원의 반지름 
T = int(input())
for i in range (T) :
    x1, y1, x2, y2 = map(int, input().split())
    n = int(input())
    cnt = 0
    for j in range (n) :
        cx, cy, r = map(int, input().split())
        distance1 = ((cx - x1) ** 2 + (cy - y1) ** 2) ** 0.5
        distance2 = ((cx - x2) ** 2 + (cy - y2) ** 2) ** 0.5
        if distance1 < r and distance2 > r:
            cnt += 1
        if distance2 < r and distance1 > r:
            cnt += 1
    print (cnt)