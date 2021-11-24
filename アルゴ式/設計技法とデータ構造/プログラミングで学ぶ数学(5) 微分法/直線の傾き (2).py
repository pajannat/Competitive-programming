# 入力
N, a, b = map(int, input().split())

for i in range(N):
    # 傾きの計算
    grad = a + b
    b = (a + b) / 2
    print(grad)