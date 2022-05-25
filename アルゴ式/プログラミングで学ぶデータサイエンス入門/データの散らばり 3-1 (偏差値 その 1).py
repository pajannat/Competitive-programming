# 入力を受け取る
X, mu, sigma = map(int, input().split())

# 答えを求める
ans = 50 + 10 * (X - mu) / sigma

# 答えを出力
print(ans)
