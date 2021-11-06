def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N, K = map(int, input().split())

    A = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append([a, b])
    
    # 安い商品から順に、購入できるだけ購入する
    A.sort()
    cnt = K
    yen = 0
    for a, b in A:
        kosu = min(cnt, b)
        cnt -= kosu
        yen += a * kosu

        # K個購入したら終了
        if cnt == 0:
            break

    # 出力
    print(yen)

if __name__ == '__main__':
    main()