def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())

    scores = {}

    for i in range(N):
        S = input().rstrip()
        if S not in scores:
            scores[S] = 1
        else:
            scores[S] += 1

    max_k = max(scores, key=scores.get)
    # 答えを出力
    print(max_k)

if __name__ == '__main__':
    main()