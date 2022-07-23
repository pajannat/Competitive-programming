def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())

    from collections import defaultdict
    counter = defaultdict(lambda: 0)

    # 処理
    # 答えを出力
    for i in range(N):
        S = input().rstrip()
        counter[S] += 1
        
        if counter[S] > 1:
            print(S + "(" + str(counter[S] - 1) + ")")
        else:
            print(S)


if __name__ == '__main__':
    main()