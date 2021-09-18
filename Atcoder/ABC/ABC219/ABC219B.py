def main():
    from sys import stdin
    input = stdin.readline

    S1 = input().rstrip()
    S2 = input().rstrip()
    S3 = input().rstrip()
    T = list(input().rstrip())
    ans = ""

    for num in T:
        if num == "1":
            ans += S1
        if num == "2":
            ans += S2
        if num == "3":
            ans += S3
    
    print(ans)

if __name__ == '__main__':
    main()