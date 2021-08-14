def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    
    if 1 <= N <= 125:
        print(4)
    elif 126 <= N <= 211:
        print(6)
    elif 212 <= N <= 214:
        print(8)

if __name__ == '__main__':
    main()