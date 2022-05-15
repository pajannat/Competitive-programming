# 正規表現を取り扱うためのライブラリ
import re 

# 入力を受け取る
N, Y, M = map(int, input().split())

YM = ''
if 1 <= M <= 9:
    YM = str(Y) + '0' + str(M)
elif 10 <= M <= 12:
    YM = str(Y) + str(M)

# 調べる正規表現 
reg = r'[^_]+(?=\_' + YM + '[0-9]{2}\.pdf$)'

for i in range(N):
    S = input().rstrip()
    # マッチした位置が格納される (存在しなければ null) 
    search = re.search(reg, S)
    if search:
        # 領収書名を出力 
        print(search.group(0))