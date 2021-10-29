def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    N = int(input())

    ans = 0
    for i in range(1, N+1):
        ans += i
    
    print(ans)
        
if __name__ == '__main__':
    main()