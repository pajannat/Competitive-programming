def main():
    from sys import stdin
    input = stdin.readline

    import math

    # 入力を受け取る
    N = int(input())

    # cnt = 0
    # # 平方数のとき、約数の数が奇数
    # for i in range(1, N+1):
    #     if i*i > N:
    #         break
    #     cnt += 1

    # print(cnt)

    # √N を求める
    sq = int(math.sqrt(N) + 1e-9)
    print(sq)

if __name__ == '__main__':
    main()