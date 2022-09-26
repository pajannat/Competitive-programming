def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    # 処理
    ans = (N-1)*(1+N-1)//2
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()