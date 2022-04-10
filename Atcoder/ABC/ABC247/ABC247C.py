def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S_list = []
    S_list.append([])

    # 処理
    for i in range(1, N+1):
        tmp = S_list[i-1] + [i] + S_list[i-1]
        S_list.append(tmp)

    # 答えを出力
    print(*S_list[-1])

if __name__ == '__main__':
    main()