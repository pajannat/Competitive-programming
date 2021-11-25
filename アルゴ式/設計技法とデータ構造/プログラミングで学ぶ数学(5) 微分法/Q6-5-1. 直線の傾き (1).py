a, b = map(int, input().split())

def f(x):
    return x**2

grad = (f(b)-f(a))/(b-a)

print(grad)