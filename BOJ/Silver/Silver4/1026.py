N = int(input())
lstA = list(map(int, input().split()))
lstB = list(map(int, input().split()))
lstB = sorted(lstB)
lstA = sorted(lstA, reverse= True)
lst = [a * b for a , b in zip(lstA, lstB)]
print(sum(lst))