def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))

    A.sort(reverse=True)

    # 処理
    ans = 0
    # まずはクーポンを無駄なく使用
    K_tmp = K
    for i in range(N):
        k = min(A[i]//X, K_tmp)
        K_tmp -= k
        A[i] -= k*X
        
    A.sort(reverse=True)

    # 大きい順に1枚ずつ使用。先頭から残り枚数分(K_tmp)は0円になる。
    ans = sum(A[K_tmp:])
    
    # 答えを出力
    print(ans)

if __name__ == '__main__':
    main()