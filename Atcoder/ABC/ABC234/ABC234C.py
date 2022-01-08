def main():
    from sys import stdin
    input = stdin.readline

    K = int(input())
    K2 = str(bin(K))[2:]
    K2 = K2.replace('1', '2')

    print(K2)

if __name__ == '__main__':
    main()