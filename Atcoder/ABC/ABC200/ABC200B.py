def main():
    from sys import stdin
    input = stdin.readline
        
    N,K = map(int,input().split())
    
    for _ in range(K):
        if N % 200 == 0:
            N = int(N / 200)
        else:
            N_str = str(N) + "200"
            N = int(N_str)

    print(N)


if __name__ == '__main__':
    main()