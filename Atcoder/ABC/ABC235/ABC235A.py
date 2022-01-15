def main():
    from sys import stdin
    input = stdin.readline

    S = input().rstrip()
    abc = list(S)
    a = abc[0]
    b = abc[1]
    c = abc[2]

    abc = int(a+b+c)
    bca = int(b+c+a)
    cab = int(c+a+b)

    print(abc+bca+cab)

if __name__ == '__main__':
    main()