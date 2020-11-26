N = int(input())
lst = list(map(int, input().split()))
if N == 1 :
    s = sum(lst) - max(lst) # 6면 - 가려지는 1면
else :
    second_lst = list(set([lst[0]+lst[1], lst[0]+lst[2], lst[0]+lst[3], lst[0]+lst[4], lst[1] + lst[2], lst[1] + lst[3], lst[1] + lst[5], lst[2] + lst[4], lst[2] + lst[5], lst[3] + lst[4], lst[3] + lst[5], lst[4] + lst[5]]))
    third_lst = list(set([lst[0]+lst[1]+lst[2], lst[0]+lst[1]+lst[3], lst[0]+lst[2]+lst[4], lst[0]+lst[3]+lst[4], lst[5]+lst[1]+lst[2], lst[5]+lst[1]+lst[3], lst[5]+lst[2]+lst[4], lst[5]+lst[3]+lst[4]]))
    # print(second_lst, len(second_lst))
    # print(third_lst, len(third_lst))
    times0_cnt = (N - 2) ** 2 * (N - 1)
    times1_cnt = (N - 2) ** 2 * 5 + (N - 2) * 4 # 3개 이상부터, 면 5개만 + 밑면에 가려지는 2가 1 
    times2_cnt = (N - 2) * 8 + 4 # 3개 이상부터, 총 8개 + 밑면에 가려지는 3이 2로
    times3_cnt = 4
    # print(times0_cnt + times1_cnt + times2_cnt + times3_cnt)
    s = times1_cnt * min(lst) + times2_cnt * min(second_lst) + times3_cnt * min(third_lst)
print(s)