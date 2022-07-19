def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    counter = [0 for _ in range(200001)]

    # 和がMとなる組み合わせの数
    ans = 0

    # 処理
    for a in A:
        counter[a] += 1
    
    # M//2まで
    # iの個数 * (M-i)の個数 をカウント
    # i == M-i の場合は (iの個数)*(iの個数-1)/2 をカウント
    for i in range(M//2+1):
        if i == M-i:
            ans += counter[i] * (counter[i] - 1) // 2
        else:
            ans += counter[i] * counter[M-i]

    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()