def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    S = input().rstrip()
    K = int(input())

    ans = ""
    for s in S:
        if s == "1":
            ans += s
        else:
            ans += s*200

    # 出力
    if K > 100:
        print(int(ans[101]))
    else:
        print(int(ans[K-1]))

if __name__ == '__main__':
    main()