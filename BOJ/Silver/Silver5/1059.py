L = int(input())
lst = sorted(list(map(int, input().split())))
print(lst)
N = int(input())

minimum = 0 # 맥시멈이 1번째 원소인 경우도 포함
for i in range (L) :
    if N > lst [i] :
        minimum = lst[i]
    elif N < lst[i] : 
        maximum = lst[i]
        break
    else : # N이 lucky set에 있는 경우
        print(0)
        exit()
left = N - minimum - 1
right = maximum - N - 1
print(left, right)
cnt = left * (right + 1) + right
print(cnt)