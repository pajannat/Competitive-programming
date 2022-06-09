def main():
    from sys import stdin
    input = stdin.readline

    from collections import Counter
    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    counter = [0 for _ in range(500000 + 1)]

    # 処理
    for a in A:
        counter[a] += 1
    
    # 最頻値をmax_cntに格納
    max_cnt = max(counter)

    # counterを0から順に調べ、
    # カウント数がmax_cntであるものが最小の最頻値
    for i in range(500000 + 1):
        if counter[i] == max_cnt:
            print(i)
            break


if __name__ == '__main__':
    main()