import sys

A, B = map(int, sys.stdin.readline().split())
a, b = A , B
while b != 0 :
    a, b = b, a % b
print (a, a *(A//a)*(B//a))