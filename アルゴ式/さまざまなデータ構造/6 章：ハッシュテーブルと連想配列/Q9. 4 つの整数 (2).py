# 入力を受け取る
N, M = map(int, input().split())
A = list(map(int,input().split()))
counter = {}

# a**2 + b**2, c**2 + d**2 で対称
# a**2 + b**2 を半分全列挙
for a in A:
    for b in A:
        counter[a**2 + b**2] = 1

flg = False
# (M-key1) == key2 <-> M == key1 + key2 となる場合があるかを探す
# (M == a**2 + b**2 + c**2 + d**2 となる場合があるかを探す)
for key in counter.keys():
    if (M - key) in counter:
        flg = True

# 答えを出力
if flg:
    print("Yes")
else:
    print("No")