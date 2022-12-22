def main():
    from sys import stdin
    input = stdin.readline

    from itertools import accumulate

    # 入力を受け取る
    D = int(input()) # イベントの開催期間 D日間
    N = int(input()) # イベントの出席者数 N人
    DD = [0]*(D+1) # 各出席者の出席期間をメモ

    # 処理

    for _ in range(N):
        L, R = map(int, input().split())
        L -= 1
        R -= 1
        DD[L] += 1
        DD[R+1] -= 1

    # 各日の出席者数の累積和
    accum_DD = list(accumulate(DD))

    # 答えを出力
    for i in range(D):
        print(accum_DD[i])


if __name__ == '__main__':
    main()