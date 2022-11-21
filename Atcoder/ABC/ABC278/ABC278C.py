def main():
    from sys import stdin
    input = stdin.readline

    from collections import defaultdict

    # 入力を受け取る
    G = defaultdict(set)
    N, Q = map(int, input().split())

    # 処理
    for _ in range(Q):
        T, A, B = map(int, input().split())
        # A が B をフォロー
        if T == 1:
            G[A].add(B)
        # A が B のフォローを解除
        elif T == 2:
            G[A].discard(B)
        # A と B が相互フォローしているかチェック
        elif T == 3:
            if B in G[A] and A in G[B]:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()