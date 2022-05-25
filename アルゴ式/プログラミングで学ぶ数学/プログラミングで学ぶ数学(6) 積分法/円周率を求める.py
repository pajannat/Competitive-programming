# 入力を受け取る
N = int(input())

# 面積を計算する
def func(x):
    return (1-x**2)**(1/2)

S = 0
for i in range(N):
    x = i/N
    S += func(x)*(1/N)

# 答え(円周率)を計算する
pi = 4*S

# 答えを出力
print(pi)