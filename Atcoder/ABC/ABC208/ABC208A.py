from sys import stdin
input = stdin.readline

A, B = map(int, input().split())

if (6*A >= B) and (B >= A):
    print("Yes")
else:
    print("No")
