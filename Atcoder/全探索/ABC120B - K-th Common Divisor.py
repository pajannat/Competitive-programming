def main():
    from sys import stdin
    input = stdin.readline
    A,B,K = map(int,input().split())
    N = max(A,B)
    num_list = []

    for num in range(1,N+1):
        if A%num==0 and B%num==0:
            num_list.append(num)

    print(num_list[-K])

if __name__ == '__main__':
    main()