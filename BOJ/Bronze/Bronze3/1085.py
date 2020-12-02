x, y, w, h = map(int, input().split())
lst = [x, y, w-x, h-y]
print(min(lst))