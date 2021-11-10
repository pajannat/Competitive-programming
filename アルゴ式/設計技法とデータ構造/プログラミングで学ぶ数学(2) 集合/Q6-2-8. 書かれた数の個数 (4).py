def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())
    ans = N -(N//3) - (N//5) + (N//15)

    # 出力
    print(ans)

if __name__ == '__main__':
    main()