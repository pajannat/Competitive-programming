# 入力を受け取る
N = int(input())
A = list(map(int, input().split()))

# 答えを求める
x = [0]*5
for a in A:
    if 0 <= a <= 20:
        x[0] += 1
    elif 21 <= a <= 40:
        x[1] += 1
    elif 41 <= a <= 60:
        x[2] += 1
    elif 61 <= a <= 80:
        x[3] += 1
    elif 81 <= a <= 100:
        x[4] += 1

# 答えを出力
for i in range(5):
    print(x[i])