def main():
    from sys import stdin
    input = stdin.readline

    import bisect

    # 入力を受け取る
    N, T = map(int, input().split())
    A = list(map(int, input().split()))
    playlist = [0]

    # 処理
    mod = sum(A)
    T = T % mod
    for i in range(N):
        tmp = A[i] + playlist[i]
        playlist.append(tmp)
    
    idx = bisect.bisect_left(playlist, T)
    num = T - playlist[max(0, idx - 1)]
    
    # 答えを出力
    print(idx, num)


if __name__ == '__main__':
    main()