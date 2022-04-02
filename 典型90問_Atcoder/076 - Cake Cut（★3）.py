def main():
    from sys import stdin
    input = stdin.readline

    from itertools import accumulate
    import bisect

    # 入力を受け取る
    N = int(input())
    A = list(map(int, input().split()))
    B = A + A
    B.pop()
    ruiseki_B = list(accumulate(B))
    sum_A = sum(A)

    # 処理

    # ケーキの大きさが10の倍数でない場合は"No"
    if sum_A % 10 != 0:
        exit(print("No"))

    # (BR-BL) = sum_A//10 <-> BR = sum_A//10 + BL となるBRを探索 
    flg = False
    for i in range(len(ruiseki_B)):
        BR = sum_A//10 + ruiseki_B[i]
        BR_idx = bisect.bisect_left(ruiseki_B, BR)
        if BR_idx >= len(ruiseki_B):
            pass
        else:
            if (ruiseki_B[BR_idx]-ruiseki_B[i]) != 0 and (ruiseki_B[BR_idx]-ruiseki_B[i]) == (sum_A//10):
                flg = True

    # 出力    
    if flg:
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()