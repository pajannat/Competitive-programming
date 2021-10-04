def main():
    from sys import stdin
    input = stdin.readline

    import math

    # 入力を受け取る
    N = int(input())

    # カードは約数の個数回ひっくり返る
    # 約数の個数が奇数のカードが裏となる

    # # 1~Nのうち裏となるカードの枚数(平方数のカード数)
    # # (平方数は約数の個数が奇数となる)
    # cnt = 0
    # for i in range(1, N+1):
    #     if i*i > N:
    #         break
    #     cnt += 1

    # √N を求める
    cnt = int(math.sqrt(N) + 1e-9)

    print(N-cnt)

if __name__ == '__main__':
    main()