def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    H, W, N = map(int, input().split())
    # defaultdict
    # 定義時の引数は, key未登録時の初期化の際に実行される関数
    from collections import defaultdict
    counter = defaultdict(lambda: 0)

    # HxWが最大200000x200000 で大きすぎる
    # コマが置かれていないマスが大半 (1 <= N <= 100000)
    # -> 座標圧縮

    # 処理
    for _ in range(N):
        X, Y = map(int, input().split())
        # 回転前の座標(X, Y)にコマを置く
        counter[str(X) + "_" + str(Y)] += 1
        # 回転後の座標(H-1-X, W-1-Y)にコマを置く
        counter[str(H-1-X) + "_" + str(W-1-Y)] += 1
    
    # 回転後も同座標にあるコマの数 ans
    ans = 0
    # コマが2個置かれているマスの数を数える
    for val in counter.values():
        if val == 2:
            ans += 1

    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()