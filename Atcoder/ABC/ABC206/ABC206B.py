def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    ans = 0
    for i in range(1,10000000):
        M = i*(i + 1)/2
        if M >= N:
            ans = i
            break
    else:
        print("見つかりませんでした。")
    print(ans)


if __name__ == '__main__':
    main()