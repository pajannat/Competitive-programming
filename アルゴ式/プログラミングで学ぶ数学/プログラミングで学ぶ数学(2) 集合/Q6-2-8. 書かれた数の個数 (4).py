def main():
    from sys import stdin
    input = stdin.readline

    # ε₯ε
    N = int(input())
    ans = N -(N//3) - (N//5) + (N//15)

    # εΊε
    print(ans)

if __name__ == '__main__':
    main()