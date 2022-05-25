# 入力を受け取る
S, h = map(int, input().split())

# f(x) = x*x*S/(h*h)
# F(x) = x**3*S/(h*h*3)
# F(h) - F(0) = S*h/3

# 答えを出力
print(S*h//3)