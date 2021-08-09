import io
import sys

_INPUT = """\
2 1
#
#
"""
sys.stdin = io.StringIO(_INPUT)


def main():
    # 入力行数が多いとき。
    from sys import stdin
    # 数値として入力一つを読み込み
    H, W = map(int, stdin.readline().rstrip().split())
    d = [stdin.readline().rstrip() for i in range(H)]

    # 平行移動が成功したかどうかを判断するフラグ
    success_flg = False
    blue = [[False for w in range(W)] for h in range(H)]
    # リストblueの値を渡す
    import copy
    blue_tmp = copy.deepcopy(blue)

    # 平行移動パターンの全探索
    for i in range(H):
        for j in range(-W+1,W):
            # 移動なしパターンを除外
            if i == 0 and j == 0:
                pass
            # 左方向への移動を除外
            elif i == 0 and j < 0:
                pass
            else:
                # すべてのマスを平行移動する
                # 最後までflg=TrueならYESを出力
                flg = True
                # マスの色を初期化
                blue_tmp = copy.deepcopy(blue)
                for h in range(H):
                    for w in range(W):
                        # マスが白色または青色の場合は判定しない
                        if d[h][w] == "." or blue_tmp[h][w]:
                            pass
                        # 平行移動して範囲内の場合に判定
                        elif h+i<H and h+i>=0 and w+j<W and w+j>=0:
                            if d[h][w] == "#" and d[h+i][w+j] == "#":
                                blue_tmp[h+i][w+j] = True
                            # 平行移動先のマスが"#"でない場合はNG
                            else:
                                flg = False
                        # 平行移動して範囲外に出る場合はNG
                        else:
                            flg = False
                # すべてのマスを平行移動させて最後までNGなし
                # 1マス以上青マスがある
                import itertools
                if flg and (True in itertools.chain.from_iterable(blue_tmp)):
                    success_flg = True                   
                        
    if success_flg:
        print("YES")
    else:
        print("NO")

if __name__ == '__main__':
    main()