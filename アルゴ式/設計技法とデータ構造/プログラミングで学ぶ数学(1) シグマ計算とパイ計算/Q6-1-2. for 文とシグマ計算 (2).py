def main():
    from sys import stdin
    input = stdin.readline

    # 入力
    L, R = map(int, input().split())

    ans = 0
    for i in range(L, R+1):
        ans += (2*i-1)**2
    
    print(ans)
        
if __name__ == '__main__':
    main()