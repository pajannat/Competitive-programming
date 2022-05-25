def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    A = list(map(int, input().split()))

    A.sort()

    # 出力
    if N%2 == 0:
        print((A[(N//2)-1] + A[N//2])/2)
    else:
        print(A[(N-1)//2])


if __name__ == '__main__':
    main()