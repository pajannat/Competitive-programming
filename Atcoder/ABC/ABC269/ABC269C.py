def main():
    from sys import stdin
    input = stdin.readline

    # 入力を受け取る
    N = int(input())
    # Nの2進数表記(str)
    str_bin_N = format(N, 'b')

    ans = []
    nums = []

    # 処理
    # str_bin_N の bin が立っている idx を調べて nums に格納
    for i, str_num in enumerate(str_bin_N):
        if str_num == '1':
            nums.append(i)

    # nums からの取り出し方のbit全探索
    # (ansの集合(bin を立てる箇所組み合わせ)のbit全探索)
    from itertools import product
    n = len(nums)
    for bits in product([0, 1], repeat=n):
        tmp_ans = ['0' for _ in range(len(str_bin_N))]
        comb = [x for x, bit in zip(nums, bits) if bit == 1]

        # binを立てる箇所(idx)の情報 comb を
        # 数字(2進数)に変換してansに格納
        for idx in comb:
            tmp_ans[int(idx)] = '1'
        ans.append(tmp_ans)
    
    # 答えを昇順にソート
    ans.sort()

    # 答えを出力
    for a in ans:
        # リスト形式の2進数を結合して文字列に変換
        join_a = ''.join(a)
        # 2進数を10進数に変換してからprint
        print(int(join_a, 2))


if __name__ == '__main__':
    main()