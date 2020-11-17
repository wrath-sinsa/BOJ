# N = int(input())
N = 3
lst = ["config.sys",
"config.inf",
"configures"]
answer = ""
# for i in range (N) :
#     file_name = input()
#     lst.append(file_name)

length = len(lst[0])
for i in range (length) :
    for j in range (N - 1) :
        # print (lst[j][i], lst[j+1][i])
        if lst[j][i] != lst[j+1][i] :
            answer += "?"
            break
    else :
        answer += lst[0][i]
        print (answer, "\n\n")
print (answer)
    