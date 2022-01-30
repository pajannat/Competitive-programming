def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    A = list(map(int, input().split()))

    ans = [0] * N

    for a in A:
        ans[a-1] += 1

    print(ans.index(3)+1)

if __name__ == '__main__':
    main()