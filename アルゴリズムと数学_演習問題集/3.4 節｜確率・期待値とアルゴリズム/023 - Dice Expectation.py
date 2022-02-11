def main():
    from sys import stdin
    input = stdin.readline

    N = int(input())
    B = list(map(int, input().split()))
    R = list(map(int, input().split()))
    
    ans = (sum(B)+sum(R))/N

    print(ans)

if __name__ == '__main__':
    main()