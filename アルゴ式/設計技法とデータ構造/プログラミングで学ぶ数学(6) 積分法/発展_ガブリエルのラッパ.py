# 入力を受け取る
n = int(input())

# 答えを求める
# s(x) = pi*x**(-2)
# S(x) = -pi*x**(-1)
# V = S(k) - S(1)
#   = pi*(-(1/k) + (1))

# 答えを出力する
print(1-1/n)