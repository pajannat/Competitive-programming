def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    Q = int(input())

    # 各Pについて x**2 + y**2 = Pとなる整数(x, y)の組み合わせ
    counter = [0 for _ in range(500001)]

    # (x, y)を全探索
    for x in range(-100, 101):
        for y in range(-100, 101):
            P = x**2 + y**2
            counter[P] += 1

    # 処理
    for _ in range(Q):
        P = int(input())
        print(counter[P])


if __name__ == '__main__':
    main()