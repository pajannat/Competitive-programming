def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    K = int(input())

    # 処理
    ans = 0
    for i in range(1, K+1):
        for j in range(1, K+1):
            if i*j <= K:
                ans += K//(i*j)
            else:
                break
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()