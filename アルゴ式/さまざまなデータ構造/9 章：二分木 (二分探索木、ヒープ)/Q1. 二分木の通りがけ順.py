# 入力を受け取る
N = int(input())
children = [list(map(int, input().split())) for _ in range(N)]

# rec(頂点 v):
def rec(v, children):
    lv = children[v][0]
    rv = children[v][1]
    # if v が左側の子頂点 lv を持つ: rec(lv)
    if lv != -1:
        rec(lv, children)
    # 頂点 v の番号を出力する
    print(v)
    # if v が右側の子頂点 rv を持つ: rec(rv)
    if rv != -1:
        rec(rv, children)

rec(0, children)