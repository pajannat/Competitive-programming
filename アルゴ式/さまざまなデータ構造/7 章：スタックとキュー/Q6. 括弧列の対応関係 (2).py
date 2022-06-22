def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = input().rstrip()

    left_bracket_idx = []

    # 括弧の対応関係
    # bracket_cor[left_bracket_idx] = right_bracket_idx
    # bracket_cor[right_bracket_idx] = left_bracket_idx
    bracket_cor = [-1 for _ in range(N)]

    # 処理
    # 前処理.
    for i, s in enumerate(S):
        if s == "(":
            left_bracket_idx.append(i)
        elif s == ")":
            right_idx = i
            left_idx = left_bracket_idx.pop()
            # i番目の右括弧に対応する左括弧のidx
            bracket_cor[right_idx] = left_idx
            # left_idx番目の左括弧に対応する右括弧のidx
            bracket_cor[left_idx] = right_idx
    
    # クエリ処理
    Q = int(input())
    for _ in range(Q):
        k = int(input())
        # 答えを出力
        print(bracket_cor[k])


if __name__ == '__main__':
    main()