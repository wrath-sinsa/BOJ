# (100+1+ | 01)+

# def pattern1 (string) :

# def pattern2 (string) :

# T = int(input())
# for i in range (T) :
#     string = str(input())
#     lst = ["0", "1", "01"]
#     while len(string) != 0 :
#         if string[0] == "1" :
#             if len(string) < 4: # 기본 조건 처리
#                 print ("패턴이 아닙니다!!!")
#                 break
#             print(string)
#             string = string.replace(lst[1], "", 1)
#             if string[0] != "0" or string[0] != string[1]: # 0이 아니면 패턴이아니고, 01이면 패턴이아님.
#                 print("패턴이 아닙니다!")
#                 break
#             find1, find2 = 0, 1
#             while find2 - find1 == 1 : # 0을 어디까지 지워줄지 판정
#                 find1 = find2
#                 find2 = string.find(lst[0], find1 + 1)
#             string = string.replace(lst[0], "", find1+1 )  #개수는 find1 + 1개
#             print(find1, find2, string) #### find2가 -1일때 예외처리 해야함
#             if find2 == -1 :
#                 find2 = string.find(lst[1])
#                 if find2 == -1 :
#                     print("패턴이 아닙니다!!")
#                     break
#             find1 = find2 - find1 - 1 # 아까 구한거에서 제거한 현위치값 (계산)
#             find2 = string.find(lst[0], find1 + 1)
#             print(find1, find2, string)
#             ## 100001001일때 처리
#             if find2 == -1 : # 0이 두개이상이 아니라는 것은, 패턴 2일 가능성이 존재
#                 string = string.replace(lst[1], "", find1)
#                 print(string)
#                 continue
#             elif find2 - find1 > 1 : # 0이 두개연속으로 있지 않으면 1을 다지워줌 >> 0 패턴으로 감
#                 string = string.replace(lst[1], "", find1)
#                 continue
#             else : # 0이 두개 연속. 1 을 하나 남김 >> 1 패턴으로 감
#                 if find1 == 1 :
#                     print("패턴이 아닙니다!!!!")
#                     break
#                 string = string.replace(lst[1], "", find1 - 1)
#                 continue
#         elif string[0] == "0" :
#             print(string)
#             if len(string) == 1 : # 기본 조건 처리
#                 print ("패턴이 아닙니다!!!")
#                 break
#             string = string.replace(lst[2], "", 1)
#     else :
#         print ("패턴입니다!")


T = int(input())
for i in range (T) :
    string = str(input())
    lst = ["0", "1", "01"]
    while len(string) != 0 :
        if string[0] == "1" :
            if len(string) < 4: 
                print ("NO")
                break
            string = string.replace(lst[1], "", 1)
            if string[0] != "0" or string[0] != string[1]:
                print("NO")
                break
            find1, find2 = 0, 1
            while find2 - find1 == 1 :
                find1 = find2
                find2 = string.find(lst[0], find1 + 1)
            string = string.replace(lst[0], "", find1+1 )
            if find2 == -1 :
                find2 = string.find(lst[1])
                if find2 == -1 :
                    print("NO")
                    break
            find1 = find2 - find1 - 1
            find2 = string.find(lst[0], find1 + 1)
            if find2 == -1 : 
                string = string.replace(lst[1], "", find1)
                continue
            elif find2 - find1 > 1 :
                string = string.replace(lst[1], "", find1)
                continue
            else :
                if find1 == 1 :
                    print("NO")
                    break
                string = string.replace(lst[1], "", find1 - 1)
                continue
        elif string[0] == "0" :
            if len(string) == 1 or string[0] == string[1] :
                print ("NO")
                break
            string = string.replace(lst[2], "", 1)
    else :
        print ("YES")