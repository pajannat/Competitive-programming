def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())

    flg_prime = True
    for i in range(2, int(N**0.5)+1):
        if N % i == 0:
            flg_prime = False
            break
    
    if flg_prime:
        print("Yes")
    else:
        print("No")

if __name__ == '__main__':
    main()