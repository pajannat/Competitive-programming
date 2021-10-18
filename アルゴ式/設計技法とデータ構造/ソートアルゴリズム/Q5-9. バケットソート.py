def main():
    from sys import stdin
    input = stdin.readline

    def bucket_sort(A):
        # 1. 長さ X の配列 num を用意し、各要素を 0 で初期化する。
        X = len(A) + 1
        num = [0]*X

        # 2. i=0,1,⋯,X−2 について、num[A[i]] の値を 1 増やす。
        #    (num[i] には A[i] = i を満たす正整数 j の個数が格納される。)
        for i in range(X-1):
            num[A[i]] += 1

        # 3. 長さ X の配列 acc を用意し、各要素を 0 で初期化する。
        acc = [0]*X

        # 4. i=1,2,⋯,X−1 について、次のように acc[i] を更新する。
        #    (acc[i] には A[i]<=i を満たす正整数 j の個数が格納される。
        for i in range(1, X):
            # 1. i=0 のとき、 acc[i]=num[i]
            if i == 0:
                acc[i] = num[i]
            # 2. i!=0 のとき、acc[i]=acc[i−1]+num[i]
            else:
                acc[i] = acc[i-1] + num[i]

        # 5. 長さが N の配列 B を用意する。
        N = len(A)
        B = [0]*N
        
        # 6. i=0,1,⋯,N−1 について、次のように B を更新する。
        for i in range(N):
            # 1. acc[A[i]] の値を 1 減らす。
            acc[A[i]] -= 1
            # 2. B[acc[A[i]]] に A[i] の値を代入する。
            B[acc[A[i]]] = A[i]
        # 7. 配列 B の値を返却する。
        return B
    
    N = int(input())
    A = list(map(int, input().split()))

    print(*bucket_sort(A))

if __name__ == '__main__':
    main()