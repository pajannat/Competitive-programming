def main():
    from sys import stdin
    input = stdin.readline

    MOD = 1000000007

    # 入力を受け取る
    N = int(input())

    # フィボナッチ数列のn項目を計算
    a = [None]*(N+1)
    a[1] = 1
    a[2] = 1

    for i in range(3, N+1):
        a[i] = (a[i-1] + a[i-2]) % MOD

    # 答えを出力
    print(a[N])

if __name__ == '__main__':
    main()