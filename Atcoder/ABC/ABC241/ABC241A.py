def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    A = list(map(int, input().split()))

    ans = 0
    for _ in range(3):
        ans = A[ans]

    print(ans)

if __name__ == '__main__':
    main()