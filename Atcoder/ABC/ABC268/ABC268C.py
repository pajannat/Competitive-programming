def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    P = list(map(int, input().split()))
    answers = [0 for i in range(N)]

    # 処理
    # 料理 pi の初期配置は i
    for i, pi in enumerate(P):
        answers[(pi-1-i) % N] += 1
        answers[(pi-i) % N] += 1
        answers[(pi+1-i) % N] += 1
    
    # 答えを出力
    print(max(answers))


if __name__ == '__main__':
    main()