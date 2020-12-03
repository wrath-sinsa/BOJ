x1, y1, x2, y2, x3, y3 = map(int, input().split())
if x1 == x2 and y1 == y2 or x1 == x3 and y1 == y3 or x2 == x3 and y2 == y3  :
    print(-1)
    exit()
elif x1 == x2 == x3 or y1 == y2 == y3 :
    print(-1)
    exit()
dist1 = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5 
dist2 = ((x3 - x1) ** 2 + (y3 - y1) ** 2) ** 0.5 
dist3 = ((x3 - x2) ** 2 + (y3 - y2) ** 2) ** 0.5 
lst = [abs(dist2 - dist1), abs(dist3 - dist1), abs(dist3 - dist2)]
print(max(lst) * 2)