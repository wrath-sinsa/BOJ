import sys

N = int(sys.stdin.readline())
scores = list(map(int, sys.stdin.readline().split()))
print(sum(scores)/max(scores)*100/len(scores))