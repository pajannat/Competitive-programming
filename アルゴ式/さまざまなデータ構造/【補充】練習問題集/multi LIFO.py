def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    # ランレングス圧縮
    A_compression = []
    for a in A:
        A_compression.append([a, 1])
    
    len_A_compression = len(A)

    # 処理
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Push query
        if flg == 0:
            v, k = int(query[1]), int(query[2])
            # ランレングス圧縮に形式で挿入
            A_compression.append([v, k])
            len_A_compression += k

        # Pop query
        elif flg == 1:
            k = int(query[1])
            # 数列に含まれる要素数が k 未満である場合,
            # "Error"と出力する
            if len_A_compression < k:
                print("Error")

            # 数列の末尾から k 個分の要素の総和を求めて、
            # それらの要素をすべて削除
            else:
                # 要素数がkになるまで要素を取り出す
                cnt = 0
                ans = 0
                while cnt < k:
                    # 末尾の連続項の数 n > k-cnt のとき
                    if A_compression[-1][1] > (k-cnt):
                        A_compression[-1][1] -= (k-cnt)
                        ans += A_compression[-1][0]*(k-cnt)
                        cnt += (k-cnt)

                    else:
                        A_compression_last = A_compression.pop()
                        ans += A_compression_last[0]*A_compression_last[1]
                        cnt += A_compression_last[1]
                        
                len_A_compression -= k
                print(ans)


if __name__ == '__main__':
    main()