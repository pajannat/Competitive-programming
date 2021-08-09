def main():
    from sys import stdin
    input = stdin.readline
    S = input().rstrip()

    ACGT_chk = set(["A","C","G","T"])
    ACGTlen_max = 0

    for S_tmp_len in range(1,len(S)+1):
        for idx in range((len(S)-S_tmp_len+1)):
            S_tmp = S[idx:idx+S_tmp_len]

            # Sの部分文字列S_tmpがACGT文字列であるかチェック
            if all([i in ACGT_chk for i in set(S_tmp)]):
                if len(S_tmp) > ACGTlen_max:
                    ACGTlen_max = len(S_tmp)

    print(ACGTlen_max)

if __name__ == '__main__':
    main()