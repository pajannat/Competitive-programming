def main():
    from sys import stdin
    input = stdin.readline


    # hash値へ変換する関数
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

    T_list = [[] for _ in range(M+1)]

    # 処理
    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Insert query
        if flg == 0:
            T = query[1]
            T_list[convert_to_hash(T)].append(T)

        # Delete query
        elif flg == 1:
            T = query[1]
            if T_list[convert_to_hash(T)] != 0:
                T_list[convert_to_hash(T)].remove(T)

        # Find query
        elif flg == 2:
            T = query[1]
            if T in T_list[convert_to_hash(T)]:
                print("Yes")
            else:
                print("No")


if __name__ == '__main__':
    main()