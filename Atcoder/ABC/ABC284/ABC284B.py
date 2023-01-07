def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    T = int(input())
    for i in range(T):
        N = int(input())
        A = list(map(int, input().split()))
        cnt = 0

        # 処理
        for a in A:
            if a % 2 != 0:
                cnt += 1
        
        # 答えを出力
        print(cnt)


if __name__ == '__main__':
    main()