def main():
    from sys import stdin
    input = stdin.readline


    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))

    # 数列 A を (整数、その個数) の形で管理するスタック
    st = []

    # 番兵を挿入する
    st.append([0, 0])

    # 数列 A の総和
    sum_A = 0

    # 現在のAをスタックに入れる
    for a in A:
        st.append([a, 1])
        sum_A += a

    Q = int(input())
    for _ in range(Q):
        query = list(input().split())

        flg = int(query[0])

        # Push query
        if flg == 0:
            v = int(query[1])

            # 数値 v をいくつ入れるか
            cnt = 1

            # stを後ろからみていき, A[i] > v である限りpop
            # popした数だけ v を挿入する
            # sum_Aの調整 -> sum_A = sum_A - popした数値 + 挿入したvの合計値
            while st[-1][0] > v:
                val, num = st.pop()
                sum_A -= val * num
                cnt += num
            
            # st に v を挿入する
            st.append([v, cnt])
            # sum_A を調整する
            sum_A += v * cnt

        # Sum query
        elif flg == 1:
            print(sum_A)


if __name__ == '__main__':
    main()