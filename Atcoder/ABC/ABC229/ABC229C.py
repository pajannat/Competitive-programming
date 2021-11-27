def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, W = map(int, input().split())

    cheese = []
    for i in range(N):
        A, B = map(int, input().split())
        cheese.append([A, B])
    
    cheese.sort(reverse=True)

    ans = 0
    for C in cheese:
        if W == 0:
            break
        
        tmp = min(C[1], W)
        W -= tmp
        ans += C[0]*tmp

    # 出力
    print(ans)

if __name__ == '__main__':
    main()