a, b = 0, 1
for i in range (int(input())) :
    a, b = b, (a +b) % 1000000
print(a)