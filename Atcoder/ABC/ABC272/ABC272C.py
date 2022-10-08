def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    even_A = []
    odd_A = []
    ans = -1

    # 処理
    for a in A:
        if a % 2 == 0:
            even_A.append(a)
        else:
            odd_A.append(a)
    
    even_A.sort()
    odd_A.sort()

    if len(even_A) >= 2:
        ans = max(ans, even_A[-1] + even_A[-2])

    if len(odd_A) >= 2:
        ans = max(ans, odd_A[-1] + odd_A[-2])
    
    # 答えを出力
    print(ans)


if __name__ == '__main__':
    main()