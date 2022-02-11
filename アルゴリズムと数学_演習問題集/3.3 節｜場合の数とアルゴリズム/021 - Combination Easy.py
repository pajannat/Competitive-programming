def main():
    from sys import stdin
    input = stdin.readline

    def fact(num):
        if num == 1 or num == 0:
            return 1
        else:
            return num*fact(num-1)

    n, r = map(int, input().split())

    ans = fact(n)//fact(r)//fact(n-r)

    print(ans)

if __name__ == '__main__':
    main()