def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N, C = input().split()
    N = int(N)
    A = input().rstrip()
    score = 0

    # 処理
    # W -> 0, B -> 1, R -> 2 とすると
    # どの操作を実行しても score は 0 or 3 変化する
    # -> score を 3で割った余りは不変
    # -> score: 0 -> W, 1-> B, 2 -> R

    # score を計算
    for a in A:
        if a == "W":
            pass
        elif a == "B":
            score += 1
        elif a == "R":
            score += 2
    
    score %= 3
    
    # 答えを出力
    flg = False
    if C == "W":
        if score == 0:
            flg = True
    elif C == "B":
        if score == 1:
            flg = True
    elif C == "R":
        if score == 2:
            flg = True
    
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()