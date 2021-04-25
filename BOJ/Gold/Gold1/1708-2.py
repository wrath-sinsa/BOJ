import sys
import heapq
import math
input = sys.stdin.readline
push = heapq.heappush
pop = heapq.heappop
# list(map(int,input().split()))

# __main__

N = int(input())
N, M = map(int,input().split())

## 내부제거 알고리즘을 이용할것
