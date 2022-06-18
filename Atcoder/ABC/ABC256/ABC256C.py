def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    h1, h2, h3, w1, w2, w3 = map(int, input().split())

    # 処理
    cnt = 0
    for h1w1 in range(1, 31):
        for h1w2 in range(1, 31):
            for h2w1 in range(1, 31):
                for h2w2 in range(1, 31):
                    flg = True
                    h3w1 = w1 - (h1w1 + h2w1)
                    h3w2 = w2 - (h1w2 + h2w2)
                    # マスが正の整数とならない場合はスキップ
                    if h3w1 <= 0 or h3w2 <= 0:
                        flg = False
                    # 残りのマスを求める
                    h1w3 = h1 - (h1w1 + h1w2)
                    h2w3 = h2 - (h2w1 + h2w2)
                    h3w3 = h3 - (h3w1 + h3w2)
                    # マスが正の整数とならない場合はスキップ
                    if h1w3 <= 0 or h2w3 <= 0 or h3w3 <= 0:
                        flg = False
                    # 最後にw3をチェック
                    if (h1w3 + h2w3 + h3w3) != w3:
                        flg = False
                    
                    if flg:
                        cnt += 1
                        # print(h1w1, h1w2, h1w3)
                        # print(h2w1, h2w2, h2w3)
                        # print(h3w1, h3w2, h3w3)
                        # print()      
    
    # 答えを出力
    print(cnt)


if __name__ == '__main__':
    main()