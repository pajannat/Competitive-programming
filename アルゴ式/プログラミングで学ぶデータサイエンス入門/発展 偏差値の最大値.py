# 入力を受け取る
N = int(input())

# 答えを求める
ave = (1*100 + (N-1)*0) / N
var = (1*(100-ave)**2 + (N-1)*(0-ave)**2) / N
SD = var**0.5

ans = 50 + 10*(100-ave)/SD

# 答えを出力
print(ans)