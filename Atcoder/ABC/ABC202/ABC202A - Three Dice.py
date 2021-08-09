def main():
    from sys import stdin
    input = stdin.readline

    A,B,C = map(int,input().split())
    A = 7-A
    B = 7-B
    C = 7-C

    print(A+B+C)
        
if __name__ == '__main__':
    main()