def main():
    from sys import stdin
    input = stdin.readline
    
    N = int(input())
    A_list = list(map(int,input().split()))

    A_squared = 0
    for num in A_list:
        A_squared += num**2

    A_sum = sum(A_list)
    A_products = int((A_sum**2 - A_squared)/2)

    ans = (N-1)*A_squared - 2*A_products
    print(ans)

if __name__ == '__main__':
    main()