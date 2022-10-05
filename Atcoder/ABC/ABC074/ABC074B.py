def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    K = int(input())
    X = list(map(int, input().split()))
    ans = 0

    # 処理
    for x in X:
        ans += 2*min(x, K-x)
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()