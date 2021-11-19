a, b = map(int, input().split())


ans = -1
if a > b:
    ans = 2
elif b >= a > -b:
    ans = 1
else:
    ans = 3

print(ans)
