N, T = int(input())
lst = []
for i in range (N) :
    tmp_lst = list(map(int, split()))
    lst.append(tmp_lst)
# 리스트에 T일에 걸친 증가량을 다 적음.
# 합이 가장 크게 구함

## 1. 예제
# 3 4, 1 2
# 1을 계속먹다가 3을 마지막에

## 2.
# 3 4, 7 2 같은 경우 
# 7을 뽑았을때 증가량은 2가아닌 7이므로
# 7을 계속뽑다가 마지막날에 3 + 4a만큼 먹음 
# 는 문제에서 제외 ㅎㅎ,,,

## 3.
# 3 4, 7 9
# 3을 먹다가 증가한 7을 마지막날에

### 1 - 3은 위치만 바뀐경우

## 4.
# 3 5, 5 5 ,pi가 같은경우
# 5를 계속먹다가 증가한 3을마지막에
# wi가 큰걸 먹는게 이득

################### 3개 이상에서는?