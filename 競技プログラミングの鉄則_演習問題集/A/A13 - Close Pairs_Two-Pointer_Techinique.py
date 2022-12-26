def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0

    # 処理
    # しゃくとり法
    R_i = 0
    # 左側を1つずつずらす
    for i in range(N):
        # 右側をひとつずつずらす
        for r_i in range(R_i, N):
            # 右側のidx更新
            R_i = r_i

            # A[r_i] - A[i] > K となりひとつ通り過ぎた場合は
            # R_i = r_i - 1 として、ひとつ巻き戻して探索終了
            if A[r_i] - A[i] > K:
                R_i = r_i - 1
                break
        
        # 左側iのときの右側R_iが確定したので、
        # ans に加算
        ans += (R_i - i)


    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()