# 正規表現を取り扱うためのライブラリ
import re 

# 調べたい文字列 
S = input().rstrip()
# 置き換える文字列
T = 'ra'
# 調べる正規表現 
reg = r'ru(?=r)'

# 置換する正規表現、置換後の文字、置換対象 の順
result = re.sub(reg, T, S)
# algomethod が出力される
print(result)