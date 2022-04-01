def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, K = map(int, input().split())
    A = []
    B = []
    C = []

    score = 0

    for i in range(N):
        a, b = map(int, input().split())
        C.append(b)
        C.append(a-b)
    
    C.sort(reverse=True)

    for i in range(2*N):
        if K >= 1:
            K -= 1
            score += C[i]
    
    print(score)

if __name__ == '__main__':
    main()