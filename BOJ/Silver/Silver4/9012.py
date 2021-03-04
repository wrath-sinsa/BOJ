T = int(input())

for i in range (T) :
    stack_list = [] 
    line = list(input())
    while len(line) != 0:
        if line[0] == "(" :
            stack_list.append(line.pop(0))
        else : 
            if len(stack_list) != 0 :
                line.pop(0)
                stack_list.pop() # 후입선출 스택
            else :
                ans = "NO"
                break
    else : 
        if len(stack_list) == 0 : ans = "YES"
        else : ans = "NO"
    print(ans)