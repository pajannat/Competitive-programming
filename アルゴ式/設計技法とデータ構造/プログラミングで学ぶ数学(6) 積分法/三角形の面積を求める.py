d, h = map(int, input().split())
# f(x) = x * (d/h)
# F(x) = (1/2)* x*x * (d/h)

def F(x):
    return (1/2)* x*x * (d/h)

ans = int(F(h) - F(0))

print(ans)