# 入力を受け取る
mu, sigma, a0, a1 = map(int, input().split())

# 答えを求める
mu_to = mu * a1 + a0
sigma_to = sigma * a1

# 答えを出力
mu_to = mu * a1 + a0
print(mu_to, sigma_to)