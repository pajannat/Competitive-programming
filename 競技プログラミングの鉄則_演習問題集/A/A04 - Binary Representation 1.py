def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    ans = ""

    # 処理
    for i in range(10):
        # 2進数として考えたとき、下i桁を削る
        tmp_num = N // 2**i

        # 2進数として考えたとき、下1桁が0か1かを判定
        tmp_num %= 2

        # ans に追記
        ans = str(tmp_num) + ans
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()