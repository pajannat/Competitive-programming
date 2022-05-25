# 入力を受け取る
X, Y = map(int, input().split())

# 答えを求める
ans = 0
for red in range(1, 7):
    for blue in range(1, 7):
        if (red + blue == X) or (red + blue == Y):
            ans += 1

# 答えを出力
print(ans)