def main():
    from sys import stdin
    input = stdin.readline


    from collections import deque
    # 入力を受け取る
    N, Q = map(int, input().split())
    S = input().rstrip()
    head = 0

    # 処理
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # query1
        if flg == 1:
            head -= int(query[1])
            head = head % N

        # query2
        elif flg == 2:
            prt_idx = head + int(query[1]) - 1
            prt_idx = prt_idx % N
            print(S[prt_idx])


if __name__ == '__main__':
    main()