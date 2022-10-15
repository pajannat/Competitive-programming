def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    ans = 1

    # 処理
    for i in range(1, N+1):
        ans *= i
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()