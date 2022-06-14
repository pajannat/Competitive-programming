def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = list(input().split())

    counter = [0 for _ in range(1000004)]
    base = ord("a")

    M = 1000003
    def convert_to_hash(s):
        s_list = list(s)
        len_s_list = len(s_list)
        hash = 0
        for idx, a in enumerate(s_list):
            # hash値に変換. a -> 1, z -> 26.
            hash = ( hash + (30**(len_s_list - idx - 1))*(ord(a) - base + 1) ) % M

        return hash

    # 処理
    for s in S:
        # 文字列sをhash値に変換してからカウント
        counter[convert_to_hash(s)] += 1

    # 答えを出力
    print(max(counter))


if __name__ == '__main__':
    main()