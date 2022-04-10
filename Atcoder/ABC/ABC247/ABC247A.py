def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    S = input().rstrip()

    # 処理
    S = "0" + S
    
    # 答えを出力
    print(S[:-1])
    
if __name__ == '__main__':
    main()