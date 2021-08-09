def main():
    from sys import stdin
    input = stdin.readline
    N = int(input())
    A = [int(i.rstrip()) for i in stdin.readlines()]
    A = set(A)

    print(len(A))

if __name__ == '__main__':
    main()
