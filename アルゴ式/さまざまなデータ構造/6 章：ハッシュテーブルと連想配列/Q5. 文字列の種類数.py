def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = set(input().split())
    
    # 答えを出力
    print(len(S))


if __name__ == '__main__':
    main()