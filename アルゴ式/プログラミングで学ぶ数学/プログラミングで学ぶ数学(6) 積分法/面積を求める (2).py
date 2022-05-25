# 入力を受け取る
L, R, a, b = map(int, input().split())

S = 0
for i in range(L,R):
    S += a*i + b

# 答えを出力
print(S)
