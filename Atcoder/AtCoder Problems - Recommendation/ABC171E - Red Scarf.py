def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    A = list(map(int, input().split()))

    xor_all = 0
    for a in A:
        xor_all = xor_all ^ a

    ans = []
    for a in A:
        ans.append(xor_all ^ a)

    print(*ans)

if __name__ == '__main__':
    main()