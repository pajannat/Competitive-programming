def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    S = list(input().split())

    counter = [0 for _ in range(27**4)]
    base = ord("a")

    def convert_to_hash(s):
        s_list = list(s)
        len_s_list = len(s_list)
        hash = 0
        for idx, a in enumerate(s_list):
            # 26進数に変換. a -> 1, z -> 26.
            hash += (27**(len_s_list - idx - 1))*(ord(a) - base + 1)

        return hash


    for s in S:
        # 文字列sをhash値に変換してからカウント
        counter[convert_to_hash(s)] += 1

    # 処理
    Q = int(input())
    for _ in range(Q):
        T = input().rstrip()
        hash_T = convert_to_hash(T)

        # 答えを出力
        print(counter[hash_T])


if __name__ == '__main__':
    main()