# 入力を受け取る
N = int(input())
scores = list(map(int, input().split()))


# 答えを求める
cnt = [[i, 0] for i in range(101)]

for s in scores:
	cnt[s][1] += 1

cnt.sort(reverse=True, key=lambda x: x[1])


# 答えを出力
for i in range(100):
	if i != 0:
		if cnt[i-1][1] > cnt[i][1]:
			break
	tmp = cnt[i][0]
	print(cnt[i][0])