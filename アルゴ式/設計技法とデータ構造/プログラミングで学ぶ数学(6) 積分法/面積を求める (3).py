# 入力を受け取る
a, b, h = map(int, input().split())

# y = (b-a)/h*x + a

# 面積を求める
for k in range(6):
    n = 10**k
    dx = h/n
    S = 0
    for i in range(n):
        x = i*(h/n)
        y = (b-a)/h*x + a
        ds = y*dx
        S += ds
    # 答えを出力
    print(S)
